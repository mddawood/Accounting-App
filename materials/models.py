from django.db import models
from django.urls import reverse
from projects.models import Project

# Create your models here.
class Material(models.Model):
    project = models.ForeignKey(Project,related_name='materials',on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    quantity = models.FloatField()
    price = models.FloatField()
    total_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.type

    def get_absolute___(self):
        return reverse("projects:detail", kwargs={'pk':self})
