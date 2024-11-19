# -*- coding: utf-8 -*-
{
    'name': "Hospital Customization Odoo 17 --",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "BEE Data",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','base_hospital_management','sale', "web",'mail',"website", "hr", "stock", "sale_management"],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        "data/ir_sequence_data.xml",
        'views/paper_format_imaging.xml',
        'views/menuitems.xml',
        'views/inpatient_view.xml',
        'views/inpatient_tree_view.xml',
        
        'views/patient_tree_view.xml',
        'views/doctor_allocation_view.xml',
        # 'views/out_patient_doctor.xml',
        
        'views/lab_test_type.xml',
        'views/lab_test_type_form_view.xml',
        'views/imaging_test_department.xml',
        'views/imaging_test_department_form_view.xml',
        
        'views/parform_imaging_view.xml',
        'views/parform_imaging_form_view.xml',
        #pdf reports
        'reports/imaging_invoice_pdf.xml',
        
        'views/test_js_menuitems.xml',
        
        
        
       
        
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'hospital_customization/static/src/js/sound_notification.js',
        #    'hospital_customization/static/src/js/js_test.js',
        #    'hospital_customization/static/src/xml/js_test.xml',
           
           # Web Cam Access
           
            # "hospital_customization/static/src/js/webcam_dialog.js",
            # "hospital_customization/static/src/js/image_field.js",
            # "hospital_customization/static/src/xml/web_widget_image_webcam.xml",
            
            
            
            "hospital_customization/static/src/js/test_cam.js",
            "hospital_customization/static/src/xml/test_cam.xml",
        ],
    },
   
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

