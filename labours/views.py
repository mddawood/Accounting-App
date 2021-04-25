from django.shortcuts import render
from projects.models import Project
from . models import Labour, Payment
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from labours.forms import LabourForm, PaymentForm
# Create your views here.

class LabourDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'labour'
    model = Labour
    template_name = 'labours/labour_detail.html'

class LabourUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('name', 'type', 'wage')
    model = Labour

class LabourDeleteView(LoginRequiredMixin, DeleteView):
    model = Labour
    success_url = reverse_lazy('projects:p_list')

@login_required
def LabourCreateView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = LabourForm(request.POST)
        if form.is_valid():
            labour = form.save(commit=False)
            labour.project = project
            labour.save()
            return redirect('projects:p_detail', slug=project.slug)
    else:
        form = LabourForm()
    return render(request, 'labours/labour_form.html', {'form': form})

@login_required
def PaymentCreateView(request, pk):
    labour = get_object_or_404(Labour, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.labour = labour
            payment.save()
            labour.total_pay += payment.total
            labour.save()
            return redirect('labours:l_detail', pk=labour.pk)
    else:
        form = PaymentForm()
    return render(request, 'labours/payment_form.html', {'form': form})

@login_required
def PaymentDeleteView(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        l_pk = payment.labour.pk
        payment.delete()
        return redirect('labours:l_detail', pk=l_pk)
    return render(request, 'labours/payment_delete.html', {'labour':payment.labour})
