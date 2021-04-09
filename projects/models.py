from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    client_name = models.CharField(max_length=200)
    start_date = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:p_detail", kwargs={'pk':self.pk})
