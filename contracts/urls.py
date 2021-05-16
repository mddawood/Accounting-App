from django.urls import path
from contracts import views

app_name = 'contracts'

urlpatterns = [
    path('<int:pk>/', views.ContractDetailView.as_view(), name='c_detail'),
    path('<slug>/c_create', views.ContractCreateView, name='c_create'),
    path('c_update/<int:pk>', views.ContractUpdateView, name='c_update'),
    path('c_delete/<int:pk>', views.ContractDeleteView, name='c_delete'),
    path('<int:pk>/pay/', views.PaymentCreateView, name='pay'),
    path('pay_del/<int:pk>', views.PaymentDeleteView, name='pay_del'),
]
