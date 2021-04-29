from django.db import models
from django.urls import reverse
from projects.models import Project
from django.utils import timezone
import datetime
from django.utils.translation import gettext as _

# Create your models here.
class Material(models.Model):
    project = models.ForeignKey(Project,related_name='materials',on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    quantity = models.FloatField()
    price = models.FloatField()
    total_price = models.FloatField(blank=True, null=True)
    due = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse(
            "materials:m_detail",
            kwargs={
                "pk": self.pk
            }
        )

class Payment(models.Model):
    material = models.ForeignKey(Material, related_name='payments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    amount = models.FloatField()
    amount_due = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        mat = self.material
        mat.due = mat.due - self.amount
        self.amount_due = mat.due
        mat.save()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "materials:m_detail",
            kwargs={
                "pk": self.material.pk
            }
        )
