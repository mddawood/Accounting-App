from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.CBView.as_view(), name='m_list'),
]
