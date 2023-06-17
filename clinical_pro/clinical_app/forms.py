from django import forms
from clinical_app.models import Patient,ClinicalData

class Patient_form(forms.ModelForm):
    class Meta:
        model=Patient
        fields= '__all__'


class ClinicalData_form(forms.ModelForm):
    class Meta:
        model=ClinicalData
        fields='__all__'