from django import forms

class DateRangeForm(forms.Form):
    start_date = forms.DateField(
        label="Start Date",
        required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
    end_date = forms.DateField(
        label="End Date",
        required=False,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
    )
