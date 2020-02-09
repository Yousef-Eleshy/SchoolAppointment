# -*- coding: utf-8 -*-
{
    'name': "website_appointment",

    'summary': """
       Appointment""",

    'description': """
        Website Appointment Booking
    """,

    'author': "EgyMentors",
    'website': "egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_calendar',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/templates.xml',
    ],
}
