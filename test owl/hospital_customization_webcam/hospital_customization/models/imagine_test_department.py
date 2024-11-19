from odoo import models, fields

class ImagingTestDepartment(models.Model):
    _name = 'imaging.test.departments'
    _description = 'Imaging Test Departments'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Imaging Test Department Name', required=True, tracking=True)
