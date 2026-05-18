from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from .forms import DiagnosisForm
from .services import SERVICES
from .utils import send_to_odoo_crm


def diagnosis_view(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            instance = form.save()
            send_to_odoo_crm(instance)

            return redirect('success_page')
    else:
        form = DiagnosisForm()

    return render(request, 'diagnosis_form.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diagnosis_form'] = kwargs.get('form', DiagnosisForm())

        context['services'] = [
            {"name": "Business Consulting & Strategy", "icon": "bi-briefcase"},
            {"name": "Sales System Development", "icon": "bi-graph-up-arrow"},
            {"name": "Marketing System Design", "icon": "bi-megaphone"},
            {"name": "HR & Workforce Systems", "icon": "bi-people"},
            {"name": "Accounting & Compliance Systems", "icon": "bi-calculator"},
            {"name": "IT & ERP Solutions", "icon": "bi-hdd-network"},
            {"name": "Operations Management", "icon": "bi-gear"},
            {"name": "Training & Capability Development", "icon": "bi-mortarboard"},
        ]
        context['methodology'] = [
            {'num': '01', 'title': 'Diagnose',
             'desc': 'Identify gaps, inefficiencies, and structural issues.',
             'image': 'img/methodology/diaganose.jpeg'},
            {'num': '02', 'title': 'Design',
             'desc': 'Create tailored business architecture and system frameworks.',
             'image': 'img/methodology/design.jpeg'},
            {'num': '03', 'title': 'Develop',
             'desc': 'Build processes, tools, and operational models.',
             'image': 'img/methodology/develop.jpeg'},
            {'num': '04', 'title': 'Deploy',
             'desc': 'Implement systems across departments.',
             'image': 'img/methodology/deploy.jpeg'},
            {'num': '05', 'title': 'Direct',
             'desc': 'Guide leadership teams on execution and alignment.',
             'image': 'img/methodology/direct.jpeg'},
            {'num': '06', 'title': 'Drive',
             'desc': 'Monitor performance and optimize outcomes.',
             'image': 'img/methodology/drive.jpeg'},
            {'num': '07', 'title': 'Deconstruct',
             'desc': 'Continuously refine systems for long-term scalability.',
             'image': 'img/methodology/decon.jpeg'},
        ]
        context['testimonials'] = [
            {
                'quote': """
                    Handling registrations, accounts, banking, and website 
                    management became completely stress free. 
                    The professional support helped us focus more on caring for
                    children and daily activities
                """,
                'author': 'VK SHIHAB',
                'company': 'TIME FOR KIDS',
            },
            {
                'quote': """
                Clear guidance, practical CDC support, and smooth execution
                made the entire process easier.
                The transparency and business-focused approach were truly 
                valuable for us
                """,
                'author': 'Abdul Latheef',
                'company': 'BestLife',
            },
            {
                'quote': """
                    ERP implementation and operational improvements were 
                    handled in a simple and effective way.
                    Managing daily business activities has now become much 
                    smoother and more organized.
                """,
                'author': 'SANJO BABU',
                'company': 'WINHEELS FOOTWEARS',
            },
            {
                'quote': """
                    Proper systems, workflows, and processes helped our 
                    operations run without confusion or delays.
                    This gave me more freedom to focus on creating better 
                    travel experiences for customers.
                """,
                'author': 'NANDAGOPAN – Director',
                'company': 'Poyalo',
            },
            {
                'quote': """
                    Improved systems and structured workflows made our daily 
                    operations more organized and efficient.
                    The overall support and guidance helped simplify many areas 
                    of the business.
                """,
                'author': 'SINOJ – Director',
                'company': 'RAGG International',
            },

        ]
        context['faqs'] = [
            ('What does business architecture include?',
             'It involves structuring your organization, defining roles, processes, and decision systems for better clarity and scalability.'),
            ('How do HR systems improve business performance?',
             'They standardize hiring, onboarding, and performance management, ensuring consistent workforce productivity.'),
            ('What is a sales system?',
             'A structured framework that manages leads, pipelines, and conversions to create predictable revenue.'),
            ('How are marketing systems different from campaigns?',
             'Marketing systems focus on long-term lead generation frameworks rather than one-time campaign execution.'),
            ('What are IT & ERP solutions used for?',
             'They integrate business functions, automate workflows, and provide real-time data visibility.'),
            ('How does operations management improve efficiency?',
             'It streamlines workflows, reduces bottlenecks, and ensures consistent execution across teams.'),
            ('Why is accounting and compliance important?',
             'It ensures financial clarity, risk management, and adherence to regulatory requirements.'),
            ('What is capability development in organizations?',
             'It focuses on training and upskilling teams to align with systems and improve performance.'),
        ]
        return context

    def post(self, request, *args, **kwargs):
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            instance = form.save()
            send_to_odoo_crm(instance)
            messages.success(request, "Thank you! We'll be in touch shortly.")
            return self.render_to_response(
                self.get_context_data(form=DiagnosisForm())
            )
        return self.render_to_response(self.get_context_data(form=form))


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ServiceView(TemplateView):
    template_name = 'core/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['icons_list'] = [
            {'name': 'Strategy', "icon": "bi-briefcase"},
            {'name': 'Operations', "icon": "bi-graph-up-arrow"},
            {'name': 'Marketing', "icon": "bi-megaphone"},
            {'name': 'Finance', "icon": "bi-people"},
            {'name': 'Team', "icon": "bi-calculator"},
            {'name': 'Technology', "icon": "bi-gear"},
            {'name': 'Growth', "icon": "bi-mortarboard"},
        ]

        context['services_list'] = [
            {
                'number': '01',
                'icon': 'bi-building',
                'title': 'Business Consulting',
                'description': 'We help you structure business models and operating frameworks.',
                'link': '/services/business-consulting/',
                'slug': 'business-consulting',
            },
            {
                'number': '02',
                'icon': 'bi-graph-up',
                'title': 'Sales System Design',
                'description': 'We design sales systems that create pipeline and drive revenue.',
                'link': '/services/sales-system-design/',
                'slug': 'sales-system-design',
            },
            {
                'number': '03',
                'icon': 'bi-megaphone',
                'title': 'Marketing Systems',
                'description': 'We build marketing systems that attract, engage and convert.',
                'link': '/services/marketing-systems/',
                'slug': 'marketing-systems',
            },
            {
                'number': '04',
                'icon': 'bi-people',
                'title': ' HR & Workforce Systems',
                'description': 'We create people systems that build strong and aligned teams.',
                'link': '/services/hr-people-systems/',
                'slug': 'hr-people-systems',
            },
            {
                'number': '05',
                'icon': 'bi-gear',
                'title': 'Accounting & Compliance',
                'description': 'We simplify processes to improve efficiency and reduce cost.',
                'link': '/services/accounting-compliance/',
                'slug': 'accounting-compliance',
            },
            {
                'number': '06',
                'icon': 'bi-laptop',
                'title': 'IT & ERP Solutions',
                'description': 'We implement the right technology to streamline operations.',
                'link': '/services/it-erp-solutions/',
                'slug': 'it-erp-solutions',
            },
            {
                'number': '07',
                'icon': 'bi-mortarboard',
                'title': 'Operations Management',
                'description': 'We upskill teams with practical training and learning tools.',
                'link': '/services/operations-management/',
                'slug': 'operations-management',
            },
            {
                'number': '08',
                'icon': 'bi-bar-chart',
                'title': 'Training & Development',
                'description': 'We help you set goals, track metrics and achieve growth.',
                'link': '/services/training-development/',
                'slug': 'training-development'
            },
        ]

        return context


class ServiceDetailView(TemplateView):
    """
    Individual service detail page
    """
    template_name = 'core/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        service = SERVICES.get(slug)
        if not service:
            raise Http404("Service not found")
        context['service'] = service
        context['slug'] = slug
        return context


class ContactView(TemplateView):
    template_name = "core/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = kwargs.get('form', DiagnosisForm())
        return context

    def post(self, request, *args, **kwargs):
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            instance = form.save()
            send_to_odoo_crm(instance)
            messages.success(request, "Thank you! We'll be in touch shortly.")
            return self.render_to_response(
                self.get_context_data(form=DiagnosisForm())
            )
        return self.render_to_response(self.get_context_data(form=form))
