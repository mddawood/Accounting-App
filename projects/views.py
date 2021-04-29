from . models import Project
from materials.models import Material
from django.urls import reverse_lazy, reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'projects'
    model = Project

class ProjectDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'project_details'
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    fields = ("project_name","client_name","start_date","address", "estimated")
    model = Project

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("project_name","client_name","start_date","address", "estimated")
    model = Project
    template_name = 'projects/project_form.html'

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects:p_list')

class SearchResultsView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Project.objects.filter(
            Q(project_name__icontains=query) | Q(client_name__icontains=query)
        )
        return object_list
