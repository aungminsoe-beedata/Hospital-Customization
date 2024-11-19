from odoo import models, fields, api
from datetime import date, timedelta

class HospitalPatientFormViewInherit(models.Model):
    _inherit = 'res.partner'

    nrc =fields.Char(string='NRC')
    father_name = fields.Char(string='Father Name')
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_age", store=True, help='Age of Patient')
    
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                birth_date = record.date_of_birth
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

    def _inverse_age(self):
        for record in self:
            if record.age:
                today = date.today()
                birth_date = today - timedelta(days=record.age * 365)
                record.date_of_birth = birth_date
            else:
                record.date_of_birth = False
       
    @api.depends('name', 'patient_seq')
    def _compute_display_name(self):
        for patient in self:
            patient.display_name = False if not patient.name else (
                '{}{}'.format(
                    patient.patient_seq and '[%s] ' % patient.patient_seq or '', patient.name
                ))
            
            
            
  
                
                
    
                

