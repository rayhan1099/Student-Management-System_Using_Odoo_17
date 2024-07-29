# __manifest__.py
{
    'name': 'Student Information Management',
    'version': '1.0',
    'summary': 'Manage student information',
    'description': 'A module to manage student information in Odoo.',
    'author': 'Your Name',
    'website': '',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sutdent_list.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
