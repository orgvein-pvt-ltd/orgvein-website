from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import DiagnosisForm


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
        context['methodology_traits'] = [
            'Data-driven', 'Customized', 'Measurable', 'Sustainable'
        ]
        context['testimonials'] = [
            {
                'quote': """
                    Before working with Orgvein, our operations lacked structure
                    and clarity. Their systematic approach transformed the way our
                    teams function. We now have clear processes, better visibility,
                    and improved performance across departments.
                """,
                'author': 'Managing Director',
                'company': 'Growing Enterprise',
            },
            {
                'quote': """
                    Orgvein didn't just advise they built systems that actually
                    work. The impact on our sales and operations has been
                    significant.
                """,
                'author': 'Operations Head',
                'company': 'Regional Business',
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
            form.save()
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
                'title': 'Business Architecture',
                'description': 'We help you structure business models and operating frameworks.',
                'link': '#'
            },
            {
                'number': '02',
                'icon': 'bi-graph-up-arrow',
                'title': 'Sales System Design',
                'description': 'We design sales systems that create pipeline and drive revenue.',
                'link': '#'
            },
            {
                'number': '03',
                'icon': 'bi-megaphone',
                'title': 'Marketing Systems',
                'description': 'We build marketing systems that attract, engage and convert.',
                'link': '#'
            },
            {
                'number': '04',
                'icon': 'bi-people',
                'title': 'HR & People Systems',
                'description': 'We create people systems that build strong and aligned teams.',
                'link': '#'
            },
            {
                'number': '05',
                'icon': 'bi-gear',
                'title': 'Process Optimization',
                'description': 'We simplify processes to improve efficiency and reduce cost.',
                'link': '#'
            },
            {
                'number': '06',
                'icon': 'bi-laptop',
                'title': 'Technology Enablement',
                'description': 'We implement the right technology to streamline operations.',
                'link': '#'
            },
            {
                'number': '07',
                'icon': 'bi-mortarboard',
                'title': 'Training & Development (Organace)',
                'description': 'We upskill teams with practical training and learning tools.',
                'link': '#'
            },
            {
                'number': '08',
                'icon': 'bi-bar-chart',
                'title': 'Performance & Growth Strategy',
                'description': 'We help you set goals, track metrics and achieve growth.',
                'link': '#'
            },
        ]

        return context
