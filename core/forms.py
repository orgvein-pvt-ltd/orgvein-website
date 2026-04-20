from django import forms
from .models import DiagnosisRequest

SERVICE_CHOICES = [
    ('', 'Select a Service...'),
    ('Business Consulting & Strategy', 'Business Consulting & Strategy'),
    ('HR & Workforce Solutions', 'HR & Workforce Solutions'),
    ('Accounts & Financial Governance', 'Accounts & Financial Governance'),
    ('Operations Management', 'Operations Management'),
    ('Sales Systems & Enablement', 'Sales Systems & Enablement'),
    ('Marketing Systems & Demand Gen', 'Marketing Systems & Demand Gen'),
    ('IT & Technology Solutions', 'IT & Technology Solutions'),
    ('Training & Development', 'Training & Development'),
]


class DiagnosisForm(forms.ModelForm):
    service = forms.ChoiceField(choices=SERVICE_CHOICES)

    class Meta:
        model = DiagnosisRequest
        fields = ('full_name', 'phone', 'email', 'service', 'message')
