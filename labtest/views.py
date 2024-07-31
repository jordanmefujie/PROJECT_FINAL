from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import LabTest, Procedure
from .forms import LabTestForm, ProcedureForm

# Create your views here.
class LabTestListView(ListView):
    model = LabTest
    template_name = 'labtests/test_list.html'

class LabTestDetailView(DetailView):
    model = LabTest
    template_name = 'labtests/test_detail.html'

class LabTestCreateView(CreateView):
    model = LabTest
    form_class = LabTestForm
    template_name = 'labtests/test_form.html'
    success_url = '/'

class LabTestUpdateView(UpdateView):
    model = LabTest
    form_class = LabTestForm
    template_name = 'labtests/test_form.html'
    success_url = '/'

class LabTestDeleteView(DeleteView):
    model = LabTest
    template_name = 'labtests/test_confirm_delete.html'
    success_url = '/'
