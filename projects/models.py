from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Sum
import datetime
from django.utils.translation import gettext as _

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(allow_unicode = True, unique = True)
    client_name = models.CharField(max_length = 200)
    start_date = models.DateField(_("Date"), default=datetime.date.today, blank = True)
    address = models.CharField(max_length = 200)
    estimated = models.FloatField(default = 0)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("projects:p_detail", kwargs={'slug':self.slug})

    #dynamic data for material expenses
    @property
    def mat_exp(self):
        return self.materials.aggregate(total_price=Sum('total_price'))['total_price']

    #dynamic data for labour payments
    @property
    def total_pay(self):
        return self.labours.aggregate(total_pay=Sum('total_pay'))['total_pay']
