from django.db import models

class Acc_Holder(models.Model):
    acc_no = models.CharField(max_length=20)
    meter_no = models.CharField(max_length=20)
    rate_change = models.FloatField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    date_field = models.DateField()  # The date associated with the account holder's data

    def __str__(self):
        return f"{self.name} ({self.acc_no})"
