import odoorpc
import os
from dotenv import load_dotenv

load_dotenv()


def send_to_odoo_crm(instance):
    try:
        odoo = odoorpc.ODOO(os.getenv('ODOO_HOST'), port=int(os.getenv('ODOO_PORT')), protocol='jsonrpc')
        odoo.login(os.getenv('ODOO_DB'), os.getenv('ODOO_USER'), os.getenv('ODOO_PASSWORD'))

        lead_data = {
            'name': f"Diagnosis: {instance.service}",
            'contact_name': instance.full_name,
            'email_from': instance.email,
            'phone': instance.phone,
            'description': instance.message,
            'type': 'lead',
        }

        lead_id = odoo.execute('crm.lead', 'create', lead_data)
        return lead_id
    except Exception as e:
        print(f"Odoo Error: {e}")
        return None
