
{
    'name': "hr_hospital",

    'summary': """
        Hospital management""",

    'author': "Olexiy Pustovgar",
    'website': "https://github.com/olexiyodoo/hr_hospital",

    'category': 'Teching',
    'license': 'OPL-1',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/disease_data.xml',
        'views/hospital_menus.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/visit_views.xml',
        'views/disease_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/doctor_demo.xml',
        'data/patient_demo.xml',
    ],
}
