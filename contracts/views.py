from django.shortcuts import render
from projects.models import Project
from . models import Contract, Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,FormView)
from contracts.forms import ContractForm, ContractUpdateForm, PaymentForm
# Create your views here.

@login_required
def ContractCreateView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.project = project
            contract.due = contract.contract_value
            contract.total_contract_value = contract.contract_value
            contract.save()
            return redirect('projects:p_detail', slug=project.slug)
    else:
        form = ContractForm()
    return render(request, 'contracts/contract_form.html', {'form':form})

class ContractDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'contract'
    model = Contract
    template_name = 'contracts/contract_detail.html'

@login_required
def ContractUpdateView(request, pk):
    ContractOld = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractUpdateForm(request.POST)
        if form.is_valid():
            ContractNew = form.save(commit=False)
            ContractOld.total_contract_value += ContractNew.variation
            ContractOld.due = ContractOld.total_contract_value
            ContractOld.save()
            return redirect('contracts:c_detail', pk=pk)
    else:
        form = ContractUpdateForm()
    return render(request, 'contracts/contract_form.html', {'form': form})

@login_required
def ContractDeleteView(request, pk):
    contract = get_object_or_404(Contract, pk = pk)
    if request.method == "POST":
        p_slug = contract.project.slug
        contract.delete()
        return redirect('projects:p_detail', slug=p_slug)
    return render(request, 'contracts/contract_delete.html', {'contract': contract})

@login_required
def PaymentCreateView(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.contract = contract
            payment.save()
            return redirect('contracts:c_detail', pk=contract.pk)
    else:
        form = PaymentForm()
    return render(request, 'contracts/payment_form.html', {'form': form})

@login_required
def PaymentDeleteView(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        refund = payment.amount
        c_pk = payment.contract.pk      #storing contract's pk
        payment.contract.due += refund
        payment.contract.save()
        payment.delete()
        return redirect('contracts:c_detail', pk=c_pk)
    return render(request, 'contracts/payment_delete.html', {'contract':payment.contract})
