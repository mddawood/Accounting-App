from django.db import models
from django.urls import reverse
from projects.models import Project
from django.utils import timezone

# Create your models here.

class Contract(models.Model):
    project = models.ForeignKey(Project, related_name='contracts', on_delete=models.CASCADE)
    contractor_name = models.CharField(max_length=200)
    contract_type = models.CharField(max_length=200)
    contract_value = models.FloatField()
    variation = models.FloatField(default = 0.0)
    total_contract_value = models.FloatField(default = 0.0)
    due = models.FloatField(blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.contract_type

    def get_absolute_url(self):
        return reverse(
        "contracts:c_detail",
        kwargs = {
            "pk": self.pk
            }
        )

class Payment(models.Model):
    contract = models.ForeignKey(Contract, related_name='payments', on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    type = models.CharField(max_length=100, default="cash")
    amount = models.FloatField()
    amount_due = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        con = self.contract
        con.due = con.due - self.amount
        self.amount_due = con.due
        con.save()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "contracts:c_detail",
            kwargs = {
                "pk": self.contract.pk
            }
        )
