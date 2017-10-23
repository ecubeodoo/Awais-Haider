# -*- coding: utf-8 -*-
{
    'name': "Comparative Wealth Report",

    'summary': "Comparative Wealth Report",

    'description': "Comparative Wealth Report",

    'author': "Ehtisham Faisal",
    'website': "http://www.bcube.com",

    # any module necessary for this one to work correctly
    'depends': ['base', 'report','income_tax_return'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
