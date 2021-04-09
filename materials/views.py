from django.shortcuts import render
from projects.models import Project
from . models import Material
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (View, ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
# Create your views here.

# @login_required
# def MaterialList(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     print(project)
#     materials = Material.objects.filter(project.pk = pk)
#     return render(request, 'materials/material_list.html', {'materials': "hello"})


# class MaterialListView(LoginRequiredMixin, ListView):
#     context_object_name = 'materials'
#     model = Material

class MaterialDetailView(DetailView):
    context_object_name = 'material_details'
    model = Material
    template = 'materials/material_detail.html'
#
# class MaterialCreateView(CreateView):
#     fields = ('type', 'quantity', 'price')
#     model = Material
#
# class MaterialUpdateView(LoginRequiredMixin, UpdateView):
#     fields = '__all__'
#     model = Material
#
# class MaterialDeleteView(LoginRequiredMixin, DeleteView):
#     model = Material
#     success_url = reverse_lazy('m_list')

class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
