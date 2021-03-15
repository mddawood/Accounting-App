from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project_list/', views.ProjectListView.as_view(), name='list'),
    path('project_list/<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
    path('project_list/create/', views.ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete'),
]
