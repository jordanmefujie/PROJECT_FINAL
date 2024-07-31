from django import forms
from .models import LabTest, Procedure

class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ['patient_name', 'test_name', 'test_date', 'result', 'procedure']

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ['name', 'description']
