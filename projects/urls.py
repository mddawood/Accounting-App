from django.urls import path, include
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='p_list'),
    path('create/', views.ProjectCreateView.as_view(), name='p_create'),
    path('account/of/<slug>/', views.ProjectDetailView.as_view(), name='p_detail'),
    path('update/<slug>/', views.ProjectUpdateView.as_view(), name='p_update'),
    path('delete/<slug>/', views.ProjectDeleteView.as_view(), name='p_delete'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('cpay/in/<slug>', views.CpayCreateView, name='cp_create'),
    path('delcpay/<int:pk>', views.CpayDeleteView, name='cp_del'),
]
