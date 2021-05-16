from django.urls import path
from labours import views

app_name = 'labours'

urlpatterns = [
    path('<int:pk>/', views.LabourDetailView.as_view(), name='l_detail'),
    path('<slug>/create', views.LabourCreateView, name='l_create'),
    path('update/<int:pk>', views.LabourUpdateView.as_view(), name='l_update'),
    path('delete/<int:pk>', views.LabourDeleteView, name='l_delete'),
    path('<int:pk>/pay/', views.PaymentCreateView, name='pay'),
    path('pay_del/<int:pk>', views.PaymentDeleteView, name='pay_del'),
]
