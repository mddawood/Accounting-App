from django.urls import path, include
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='p_list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='p_detail'),
    path('create/', views.ProjectCreateView.as_view(), name='p_create'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='p_update'),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='p_delete'),
    # path('materials/<int:pk>', include('materials.urls', namespace='materials')),
    # path('project_list/<int:pk>/add_material/', views.add_material, name='add_material'),
]
