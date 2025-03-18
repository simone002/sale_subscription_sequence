# -*- coding: utf-8 -*-
{
    'name': "sale_subscription_sequence",
    
    'summary': " sequence for sale subscription",
  
    'license': 'OPL-1',

    'author': "STeSI Consulting",

    'category': '',
  
    'version': '18.0.0.1',
  
    'website': "https://github.com/ingegniamo/sale_subscritpion_sequence",

    # any module necessary for this one to work correctly
    'depends': ['sale'],
    
    # always loaded
    'data': ['data/sequence.xml'],

    'application': False,
    'installable': True,
}
