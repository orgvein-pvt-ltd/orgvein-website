from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problems'] = [
            'Teams become misaligned',
            'Processes break down',
            'Sales become unpredictable',
            'Operations become chaotic',
        ]
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
            'Diagnose', 'Design', 'Develop', 'Deploy', 'Direct', 'Drive',
            'Deconstruct'
        ]
        context['methodology_traits'] = [
            'Data-driven', 'Customized', 'Measurable', 'Sustainable'
        ]
        context['who_we_help'] = [
            'SME founders',
            'Startup leaders',
            'Managing directors',
            'Operations and HR heads',
        ]
        context['results'] = [
            'Streamlined operations',
            'Predictable revenue systems',
            'Improved team performance',
            'Reduced dependency on founders',
            'Scalable business infrastructure',
        ]
        return context
