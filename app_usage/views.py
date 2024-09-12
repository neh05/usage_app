from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import DateRangeForm
from .models import Acc_Holder
from datetime import datetime, timedelta
from django.db.models import Q
import json

def form_view(request: HttpRequest) -> HttpResponse:
    form = DateRangeForm(request.POST or None)
    user_details = None
    past_seven_days = Acc_Holder.objects.filter(
        date_field__gte=datetime.now() - timedelta(days=7)
    )

    if request.method == "POST" and form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]
        search_term = request.POST.get("search_term", "")

        # Filter user details by date_field if start and end dates are provided
        if start_date and end_date:
            user_details = Acc_Holder.objects.filter(date_field__range=(start_date, end_date))
        else:
            user_details = Acc_Holder.objects.all()

        # Apply search filter if search term is provided
        if search_term:
            user_details = user_details.filter(
                Q(name__icontains=search_term) |
                Q(acc_no__icontains=search_term) |
                Q(meter_no__icontains=search_term) |
                Q(rate_change__icontains=search_term) |
                Q(address__icontains=search_term) |
                Q(email__icontains=search_term) |
                Q(contact_no__icontains=search_term)
            )
        
        return render(request, "calendar.html", {
            "form": form,
            "user_details": user_details,
            "selected_start_date": start_date.strftime("%d %b %Y") if start_date else None,
            "selected_end_date": end_date.strftime("%d %b %Y") if end_date else None,
            "past_seven_days": past_seven_days,
            "search_term": search_term
        })

    ctx = {
        "form": form,
        "past_seven_days": past_seven_days,
        "search_term": ""
    }
    return render(request, "calendar.html", ctx)

def daily_usage(request):
    acc_holder = Acc_Holder.objects.all()
    chart_data = [['Date', 'Rate_Change']]

    for i in acc_holder:
        chart_data.append([i.date_field, i.rate_change])
    
    # chart_data_json = json.dumps(chart_data)
    
    return render(request, 'excess_usage_detail.html')

