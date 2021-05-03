from django.urls import path
from contracts import views

app_name = 'contracts'

urlpatterns = [
    path('<int:pk>/', views.ContractDetailView.as_view(), name='c_detail'),
    path('<slug>/c_create', views.ContractCreateView, name='c_create'),
    # path('c_update/<int:pk>', views.MaterialUpdateView, name='c_update'),
]
