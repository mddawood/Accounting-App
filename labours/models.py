from django.db import models
from django.urls import reverse
from projects.models import Project
from django.utils import timezone
from django.db.models import Sum

# Create your models here.
class Labour(models.Model):
    project = models.ForeignKey(Project,related_name='labours',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    wage = models.FloatField()
    total_pay = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "labours:l_detail",
            kwargs={
                "pk": self.pk
            }
        )


class Payment(models.Model):
    labour = models.ForeignKey(Labour, related_name='payments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    days = models.FloatField()
    total = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        lbr = self.labour
        self.total = lbr.wage * self.days
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "labours:l_detail",
            kwargs={
                "pk": self.labour.pk
            }
        )
