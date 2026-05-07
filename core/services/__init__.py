from .business_consulting import SERVICE as business_consulting
from .sales_system_design import SERVICE as sales_system_design
from .marketing_systems import SERVICE as marketing_systems
from .hr_people_systems import SERVICE as hr_people_systems
from .accounting_compliance import SERVICE as accounting_compliance
from .it_erp_solutions import SERVICE as it_erp_solutions
from .operations_management import SERVICE as operations_management
from .training_development import SERVICE as training_development

SERVICES = {
    business_consulting['slug']: business_consulting,
    sales_system_design['slug']: sales_system_design,
    marketing_systems['slug']: marketing_systems,
    hr_people_systems['slug']: hr_people_systems,
    accounting_compliance['slug']: accounting_compliance,
    it_erp_solutions['slug']: it_erp_solutions,
    operations_management['slug']: operations_management,
    training_development['slug']: training_development,
}


def get_service(slug):
    return SERVICES.get(slug)


def get_all_services():
    return list(SERVICES.values())
