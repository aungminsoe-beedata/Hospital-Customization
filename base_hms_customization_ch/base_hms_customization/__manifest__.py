# -*- coding: utf-8 -*-
{
    'name': "base_hms_customization two",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','basic_hms','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'paper_format_customize/paperformat.xml',
        'views/menuitems.xml',
        'views/medical_inpatient_investigation_tree_view.xml',
        'views/medical_inpatient_investigation_form_view.xml',
        'views/investigation_information_views.xml',
        
        'report/investigation_reports.xml',
        'views/operation_notes_view.xml',
        'views/operation_notes_tree_view.xml',
        'report/operation_notes_reports.xml',
        'views/medical_patient_view.xml',
        
        'views/patient_room_form_view.xml',
        'views/patient_room_kanban_view.xml',
        'views/patient_room_tree_view.xml',
        
        'views/medical_inpatient_registeration_form_inherit.xml',
        'views/medical_patient_tree_view_inherit.xml',
        'views/product_category_form_view_inherit.xml',
        'views/medical_physicans_form_view_inherit.xml',
        'views/medical_physicans_tree_view_inherit.xml',
        
        'views/sale_order_line_from_view_inherit.xml',
        'views/account_move_line_views.xml',
        'views/referral_payment.xml',
        
        
        # 'views/pos_order_line.xml',
       
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
     'assets': {
        'point_of_sale._assets_pos': [
                'base_hms_customization/static/src/js/pos_load_data.js',
                'base_hms_customization/static/src/js/pos_screen.js',
    #             'base_hms_customization/static/src/js/orderline.js',
    #             'base_hms_customization/static/src/js/pos_orderline.js',
                'base_hms_customization/static/src/xml/pos_screen.xml',
    #             'base_hms_customization/static/src/xml/orderline.xml',
            ],
    },
   
 
	


    
}

