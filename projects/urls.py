from django.urls import path, include
from projects import views
from materials import views as mat_view

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='p_list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='p_detail'),
    path('create/', views.ProjectCreateView.as_view(), name='p_create'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='p_update'),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='p_delete'),
    # path('<slug>/<int:pk>', mat_view.MaterialDetailView.as_view(), name='m_detail'),
    # path('materials/<int:pk>', include('materials.urls', namespace='materials')),
    # path('project_list/<int:pk>/add_material/', views.add_material, name='add_material'),
]
