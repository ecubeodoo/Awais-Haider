# -*- coding: utf-8 -*-

{
    'name': "Income Tax Returns",

    'summary': "Income Tax Return",

    'description': "Income Tax Return",

    'author': "Ehtisham Faisal, Ali",
    'website': "http://oxenlab.com",


    # any module necessary for this one to work correctly
    'depends': ['base','sale','hr','mail','fbr_details'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'sequence/sequence.xml',
        'sequence/sequence1.xml',
        'wizards/wizards.xml'
        'security/ir.model.access.csv'
        'security/income_tax_return_security.xml'
    ],
    'installable' : True,
}