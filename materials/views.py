from django.shortcuts import render
from projects.models import Project
from . models import Material, Payment
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
from materials.forms import MaterialForm, PaymentForm, MaterialUpdateForm
# Create your views here.

class MaterialDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'material'
    model = Material
    template_name = 'materials/material_detail.html'

@login_required
def MaterialUpdateView(request, pk):
    MaterialOld = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialUpdateForm(request.POST)
        if form.is_valid():
            MaterialNew = form.save(commit=False)
            if ( MaterialOld.price == MaterialNew.price ):
                MaterialOld.price = MaterialNew.price
            else:
                MaterialOld.price = MaterialNew.price

            MaterialOld.quantity += MaterialNew.quantity
            new_total = MaterialNew.price * MaterialNew.quantity
            MaterialOld.total_price += new_total
            MaterialOld.due += new_total
            MaterialOld.project.total_expense += new_total
            MaterialOld.project.save()
            MaterialOld.save()
            return redirect('materials:m_detail', pk=pk)
    else:
        form = MaterialUpdateForm()
    return render(request, 'materials/material_form.html', {'form': form})

class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material
    success_url = reverse_lazy('projects:p_list')

@login_required
def MaterialCreateView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.project = project
            material.total_price = material.price * material.quantity
            material.due = material.total_price
            material.project.total_expense += material.total_price
            material.project.save()
            material.save()
            return redirect('projects:p_detail', slug=project.slug)
    else:
        form = MaterialForm()
    return render(request, 'materials/material_form.html', {'form': form})

@login_required
def PaymentCreateView(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.material = material
            payment.save()
            return redirect('materials:m_detail', pk=material.pk)
    else:
        form = PaymentForm()
    return render(request, 'materials/payment_form.html', {'form': form})

@login_required
def PaymentDeleteView(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        refund = payment.amount
        m_pk = payment.material.pk
        payment.material.due += refund
        payment.material.save()
        payment.delete()
        return redirect('materials:m_detail', pk=m_pk)
    return render(request, 'materials/payment_delete.html', {'material':payment.material})
