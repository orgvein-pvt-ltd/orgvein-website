from django.contrib import admin
from .models import DiagnosisRequest


@admin.register(DiagnosisRequest)
class DiagnosisRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'service', 'created_at')
    search_fields = ('full_name', 'email', 'service')
