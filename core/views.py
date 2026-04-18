from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
             'desc': 'Identify gaps, inefficiencies, and structural issues.'},
            {'num': '02', 'title': 'Design',
             'desc': 'Create tailored business architecture and system frameworks.'},
            {'num': '03', 'title': 'Develop',
             'desc': 'Build processes, tools, and operational models.'},
            {'num': '04', 'title': 'Deploy',
             'desc': 'Implement systems across departments.'},
            {'num': '05', 'title': 'Direct',
             'desc': 'Guide leadership teams on execution and alignment.'},
            {'num': '06', 'title': 'Drive',
             'desc': 'Monitor performance and optimize outcomes.'},
            {'num': '07', 'title': 'Deconstruct',
             'desc': 'Continuously refine systems for long-term scalability.'},
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
        return context
