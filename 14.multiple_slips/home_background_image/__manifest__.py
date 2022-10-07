# -*- coding: utf-8 -*-
{
    'name': "Home Background Image",

    'summary': """
       This odoo app helps to add background image at home screen.""",

    'description': """
        This odoo app helps to add background image at home screen. And this module only supports odoo Enterprise version
    """,

    "author": "Cybat",
    "website" : "https://www.cybat.net",
    "price": 8.00,
    "currency": 'EUR',
    'version': '14.0.0.1',
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'application': True,
    'installable': True,
}
