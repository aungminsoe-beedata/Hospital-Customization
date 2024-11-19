from odoo import models, fields, api

class HospitalINPatientFormViewInherit(models.Model):
    _inherit = 'hospital.inpatient'

    patient_id = fields.Many2one(
        'res.partner', 
        string="Patient Name",
        domain=[('patient_seq', 'not in',
                ['New', 'Employee', 'User']),
                ('inpatient_boolean', '=', False)
                ],
        required=True, 
        help='Choose the patient'
    )

    test = fields.Boolean('Test',related = 'patient_id.inpatient_boolean',store = True)
   
    is_patient_in_draft = fields.Boolean(
        string="Is Patient in Draft", 
        compute='_compute_is_patient_in_draft', 
        store=True
    )

 