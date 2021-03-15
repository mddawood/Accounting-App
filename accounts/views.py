from . import models
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectListView(ListView):
    context_object_name = 'projects'
    model = models.Project
    template_name = 'project_list.html'

class ProjectDetailView(DetailView):
    context_object_name = 'project_details'
    model = models.Project
    template_name = 'project_detail.html'

class ProjectCreateView(CreateView):
    fields = '__all__'
    model = models.Project

class ProjectUpdateView(UpdateView):
    fields = '__all__'
    model = models.Project

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('list')
