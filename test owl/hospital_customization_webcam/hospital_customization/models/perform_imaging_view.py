from odoo import models, fields, api
from odoo.exceptions import UserError

class ImagingTestPerform(models.Model):
    _name = 'imaging.testperform'
    _description = 'Imaging Test Perform Departments'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Test', store=True, copy=False, readonly=True, index=True,
                       default=lambda self: 'New')
    web_cam_image = fields.Binary('Web Cam Image', help="Capture an image using the webcam")
    request_date = fields.Date(string='Date Requested', help='Request date', default=fields.Date.today())
    analysis_date = fields.Date(string='Date of the Analysis', help='Date of the Analysis')
    
    image_code = fields.Many2one('labtest.typeimage', string="Test Name", required=True, tracking=True)
    test_type = fields.Char(string='Test Code', related='image_code.code', store=True, readonly=True, tracking=True)
    test_price = fields.Float(string='Test Price', related='image_code.test_charge', store=True, readonly=True, tracking=True)
    test_price_currency = fields.Many2one(string='Currency', related='image_code.currency_id', store=True, readonly=True, tracking=True)
    test_price_tax = fields.Many2one('account.tax', string='Tax', related='image_code.tax_ids2', store=True, readonly=True, tracking=True)
    
    department_id = fields.Many2one('imaging.test.departments', string="Department", required=True, tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('test', 'Test In Progress'), ('completed', 'Completed'), ('invoiced', 'Invoiced')],
                             string='State', readonly=True, help='State of test imaging', default="draft")
    
    patient = fields.Many2one('res.partner', string="Patient Name", domain=[('patient_seq', 'not in', ['New', 'Employee', 'User'])], required=True, help='Choose the patient')
    doctor = fields.Many2one('hr.employee', string="Doctor", required=True, help='Name of attending doctor', domain=[('job_id.name', '=', 'Doctor')])
    
    has_image1 = fields.Binary(string="Image 1", help="Indicates if there is an image associated with this test")
    has_image2 = fields.Binary(string="Image 2", help="Indicates if there is an image associated with this test")
    has_image3 = fields.Binary(string="Image 3", help="Indicates if there is an image associated with this test")
    has_image4 = fields.Binary(string="Image 4", help="Indicates if there is an image associated with this test")
    test_information = fields.Text(string="Test Information")
    
    
    invoice_id = fields.Many2one('account.move', string='Invoice', help='Invoice for the test', copy=False)

    @api.model
    def create(self, vals):
        """Sequence number generation"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('imaging.testperform') or 'New'
        return super().create(vals)

    def action_start_test(self):
        """Change the state to 'Test In Progress'."""
        self.write({'state': 'test'})
        
    def action_cancel(self):
        """Reset the state to 'Draft'."""
        self.write({'state': 'draft'})
        
    def action_end_test(self):
        """Change the state to 'Completed'."""
        self.write({'state': 'completed'})
        
    def action_create_invoice(self):
        """Create the invoice for the patient based on the selected test."""
        # Check if 'analysis_date' is filled
        if not self.analysis_date:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Need Analysis Date',
                    'message': 'Please fill in the Analysis Date before creating the invoice.',
                    'sticky': False,  # Notification will disappear after a few seconds
                    'type': 'danger',  # This will display the message in red
                }
            }
        invoice_vals = {
            'partner_id': self.patient.id,
            'ref': self.name,
            'move_type': 'out_invoice',  # 'out_invoice' for customer invoices
            'invoice_line_ids': [(0, 0, {
                'name': self.image_code.name,  # Assuming you have a related product
                'quantity': 1,
                'price_unit': self.test_price,
                'tax_ids': [(6, 0, self.image_code.tax_ids2.ids)],  # Pass tax_ids as a Many2many tuple
            })],
        }

        # Create the invoice
        invoice = self.env['account.move'].create(invoice_vals)
        self.write({'state': 'invoiced', 'invoice_id': invoice.id})

        # Optionally, open the created invoice form
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'target': 'current',
        }
    invoice_count = fields.Integer(string='Invoice '
                                          'Count',
                                   compute='_compute_invoice_count',
                                   help='Total number of invoices for this '
                                        'patient lab test.')
    def _compute_invoice_count(self):
        """Method for computing invoice_count"""
        for record in self:
            record.invoice_count = self.env['account.move'].sudo().search_count(
                ['|', (
                    'ref', '=', record.name), ('payment_reference', '=',
                                                       record.name)])
        
    def action_view_invoice(self):
        """Method for viewing invoice from the smart button."""
        return {
            'name': 'Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            "context": {"create": False, 'default_move_type': 'out_invoice'},
            'domain': [('id', '=', self.invoice_id.id)]  # Use invoice_id to filter
        }
        
        
    def action_print_invoice(self):
        # """Method for generating the patient imaging pdf"""
        # data = {
        #     'name':self.patient.name,
        #     'code':self.name,
        #     'department':self.department_id.name,
        #     'image_code':self.image_code.name,
        #     'doctor_name':self.doctor.name,
        #     'price':self.test_price,
        #     'currency_name':self.test_price_currency.name,
        #     'img_test_code' : self.test_type,
        #     'price_tax':self.test_price_tax.name,
        #     'date':self.analysis_date,
        #     'image_one':self.has_image1,
            
        # }
        return self.env.ref(
            'hospital_customization.action_imaging_pdf_invoice'
        ).report_action(self)
