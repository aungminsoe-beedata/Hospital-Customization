from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    hospital_inpatient_id = fields.Many2one('hospital.inpatient')
    is_patient_in_draft = fields.Selection(
        string="Is Patient in Draft", 
        related='hospital_inpatient_id.state',
        store=True
    )
    
    patient_hospital_id = fields.Char(
        string="Patient In Hospital", 
        related='hospital_inpatient_id.name',
        store=True
    )
    
    attending_doctor = fields.Char(
        string="Attending Doctor", 
        related='hospital_inpatient_id.name',
        store=True
    )
    
    is_inpatient = fields.Boolean(string="Is Inpatient")
    
    inpatient_reg_ids = fields.One2many('hospital.inpatient', 'patient_id',
                                        string='Patient History Taking', store=True)
    
    
    inpatient_reg_count = fields.Boolean(
        string="Patient History Count", 
        compute='_inpatient_reg_count_cal',store =True
    )
    
    inpatient_boolean = fields.Boolean(
        string="Patient In",
        compute='_compute_inpatient_fields',store = True
    )
    
    @api.depends('inpatient_reg_ids')
    def _inpatient_reg_count_cal(self):
        """Calculate the count of related inpatient records."""
        for patient in self:
            patient.inpatient_reg_count = len(patient.inpatient_reg_ids)

    @api.depends('inpatient_reg_count','inpatient_reg_ids.state')
    @api.onchange('inpatient_reg_ids.state')
    def _compute_inpatient_fields(self):
        """Compute if the patient has any inpatient records."""
        # for record in self:
        #     record.inpatient_boolean = record.inpatient_reg_count > 0
        for record in self:
            if record.inpatient_reg_ids.state == 'dis' or not record.inpatient_reg_ids:
                
                record.inpatient_boolean = False
            else:
                record.inpatient_boolean = True
                
