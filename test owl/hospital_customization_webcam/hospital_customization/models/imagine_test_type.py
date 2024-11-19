from odoo import models, fields

class ImagineTestType(models.Model):
    _name = 'labtest.typeimage'
    _description = 'Image Lab Test Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Removed 'imaging.test.departments'

    name = fields.Char(string='Name', required=True, tracking=True,store=True)
    code = fields.Char(string='Code', required=True, tracking=True,store=True)
    department_id = fields.Many2one('imaging.test.departments', 
                                    string="Department", 
                                    required=True, tracking=True)
    test_charge = fields.Float(string='Test Charge', required=True, tracking=True,store=True)
    
    
    currency_id = fields.Many2one('res.currency', string='Currency',store=True,
                                  default=lambda self:
                                  self.env.user.company_id.currency_id.id,
                                  required=True, help='Currency in which '
                                                      'payments will be done')
    tax_ids = fields.Many2many('account.tax', string='Tax',
                               help='Tax for the test',store=True)
    tax_ids2 = fields.Many2one('account.tax', string='Tax2',
                               help='Tax for the test',store=True)
