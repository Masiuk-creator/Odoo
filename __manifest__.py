# -*- coding: utf-8 -*-
{
    'name': "Upload exchange rate",

    'summary': """
        Update currencies exchange rates from NBU and PrivatBank""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'data': [
        'views/currency.xml',
    ],
    # always loaded

    # only loaded in demonstration mode
    'demo': [
        'demo/cron.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False

}

