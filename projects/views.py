from . models import Project
from django.urls import reverse_lazy, reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'projects'
    model = Project

class ProjectDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'project_details'
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = Project
    success_url = reverse_lazy("projects:p_list")

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = Project
    success_url = reverse_lazy("projects:p_list")

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects:p_list')

##############################################
#########Function views for materials#########
##############################################

# def add_material(request, pk):
#     project = get_object_or_404(models.Project, pk=pk)
#     if request.method == "POST":
#         form = MaterialForm(request.POST)
#         if form.is_valid():
#             material = form.save(commit=False)
#             material.project = project
#             material.total_price = material.price * material.quantity
#             material.save()
#             return redirect('detail', pk=project.pk)
#     else:
#         form = MaterialForm()
#     return render(request, 'projects/material_form.html', {'form': form})
