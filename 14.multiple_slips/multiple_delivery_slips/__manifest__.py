# -*- coding: utf-8 -*-
{
    'name': "Print Multiple Copies of Delivery Slip",

    'summary': """
       This odoo app helps to print multiple copies of delivery slip with your desired text.""",

    'description': """
        This odoo app helps to print multiple copies of delivery slip.
    """,

    "author": "Cybat",
    "website" : "https://www.cybat.net",
    "price": 10.00,
    "currency": 'EUR',
    'version': '14.0.0.2',
    'depends': ['stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_slip.xml',
        'views/templates.xml',
        'views/inherited_external_layout.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'application': True,
}
