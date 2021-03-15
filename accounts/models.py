from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    start_date = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})

#one to many relationship since one project can have multiple materials
class Material(models.Model):
    type = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    project = models.ForeignKey(Project,related_name='materials',on_delete=models.CASCADE)

    def __str__(self):
        return self.type
