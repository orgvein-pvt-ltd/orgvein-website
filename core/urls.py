from django.urls import path
from .views import (
    HomeView, AboutView, ServiceView, ServiceDetailView, ContactView,
    PrivacyPolicyView, TermsOfServiceView, xml_sitemap_view
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('services', ServiceView.as_view(), name='services'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service_detail'),
    path('contact', ContactView.as_view(), name='contact'),

    # Legal & SEO Routes
    path('privacy-policy', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms-of-service', TermsOfServiceView.as_view(), name='terms_of_service'),
    path('sitemap.xml', xml_sitemap_view, name='sitemap_xml'),
]