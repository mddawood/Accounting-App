from django.urls import path
from materials import views

app_name = 'materials'

urlpatterns = [
    path('<int:pk>/', views.MaterialDetailView.as_view(), name='m_detail'),
    path('<slug>/m_create', views.MaterialCreateView, name='m_create'),
    path('m_update/<int:pk>', views.MaterialUpdateView, name='m_update'),
    path('m_delete/<int:pk>', views.MaterialDeleteView.as_view(), name='m_delete'),
    path('<int:pk>/pay/', views.PaymentCreateView, name='pay'),
    path('pay_del/<int:pk>', views.PaymentDeleteView, name='pay_del'),
]
