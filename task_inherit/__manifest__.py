{
    'name' : 'Task',
    'version' : '1.0',
    'sequence': -200,
    'description': "This is for task purpose",
    #'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['sale'],
    'data': ['views/inherit_sale_views.xml',
    'views/inherit_sale_order_line_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}