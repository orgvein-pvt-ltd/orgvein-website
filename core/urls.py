from django.urls import path
from .views import (
    HomeView, AboutView, ServiceView, ServiceDetailView, ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('services', ServiceView.as_view(), name='services'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service_detail'),
    path('contact', ContactView.as_view(), name='contact'),
]
