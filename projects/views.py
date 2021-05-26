from . models import Project, Payment, Miscellaneous
from materials.models import Material
from django.urls import reverse_lazy, reverse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.db.models import Q
from projects.forms import PaymentForm, MiscellaneousForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum

# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'projects'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['expense'] = Project.objects.all().aggregate(sum_all=Sum('total_expense')).get('sum_all')
        context['fund'] = Project.objects.all().aggregate(sum_all=Sum('total_client_payment')).get('sum_all')
        return context

class ProjectDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'project_details'
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    fields = ("serial_number", "project_name","client_name","start_date","address", "estimated")
    model = Project

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("serial_number", "project_name","client_name","start_date","address", "estimated")
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

@login_required
def CpayCreateView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.project = project
            payment.project.total_client_payment += payment.amount
            payment.project.save()
            payment.save()
            return redirect('projects:p_detail', slug=project.slug)
    else:
        form = PaymentForm()
    return render(request, 'projects/payment_form.html', {'form': form})

@login_required
def CpayDeleteView(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        p_slug = payment.project.slug #storing project slug to redirect after deletion
        payment.project.total_client_payment -= payment.amount
        payment.project.save()
        payment.delete()
        return redirect('projects:p_detail', slug=p_slug)
    return render(request, 'projects/payment_delete.html', {'project':payment.project})


@login_required
def MiscellaneousCreateView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        form = MiscellaneousForm(request.POST)
        if form.is_valid():
            miscellaneous = form.save(commit=False)
            miscellaneous.project = project
            miscellaneous.project.total_expense += miscellaneous.amount
            miscellaneous.project.save()
            miscellaneous.save()
            return redirect('projects:p_detail', slug=project.slug)
    else:
        form = MiscellaneousForm()
    return render(request, 'projects/miscellaneous_form.html', {'form': form})

@login_required
def MiscellaneousDeleteView(request, pk):
    miscellaneous = get_object_or_404(Miscellaneous, pk=pk)
    if request.method == 'POST':
        p_slug = miscellaneous.project.slug #storing project slug to redirect after deletion
        miscellaneous.project.total_expense -= miscellaneous.amount
        miscellaneous.project.save()
        miscellaneous.delete()
        return redirect('projects:p_detail', slug=p_slug)
    return render(request, 'projects/miscellaneous_delete.html', {'project':miscellaneous.project})
