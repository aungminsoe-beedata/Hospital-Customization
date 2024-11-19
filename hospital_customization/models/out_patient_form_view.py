from odoo import models, fields

class HospitalOutPatientFormViewInherit(models.Model):
    _inherit = 'hospital.outpatient'
    
    # doctor_name = fields.Many2one('doctor.allocation', string="Doctor Name")
    # doctor_id = fields.Char(related='doctor_name.doctor_id', string="Doctor ID", store=True)
