from django.shortcuts import render
from projects.models import Project
from . models import Contract, Payment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView,FormView)
from contracts.forms import ContractForm, ContractUpdateForm, PaymentForm
# Create your views here.

class ContractDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'contract'
    model = Contract
    template_name = 'contracts/contract_detail.html'

@login_required
def ContractCreateView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.project = project
            contract.due = contract.expense
            contract.save()
            return redirect('projects:p_detail', slug=project.slug)
    else:
        form = ContractForm()
    return render(request, 'contracts/contract_form.html', {'form':form})

# @login_required
# def ContractUpdateView(request, pk):
#     ContractOld = get_object_or_404(Contract, pk=pk)
#     if request.method == "POST":
#         form = MaterialUpdateForm(request.POST)
#         if form.is_valid():
#             MaterialNew = form.save(commit=False)
#             if ( MaterialOld.price == MaterialNew.price ):
#                 MaterialOld.price = MaterialNew.price
#             else:
#                 MaterialOld.price = MaterialNew.price
#
#             MaterialOld.quantity += MaterialNew.quantity
#             new_total = MaterialNew.price * MaterialNew.quantity
#             MaterialOld.total_price += new_total
#             MaterialOld.due += new_total
#             MaterialOld.save()
#             return redirect('materials:m_detail', pk=pk)
#     else:
#         form = MaterialUpdateForm()
#     return render(request, 'materials/material_form.html', {'form': form})
