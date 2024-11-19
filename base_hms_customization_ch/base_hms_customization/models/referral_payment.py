# -*- coding: utf-8 -*-
from odoo import api, fields, models
from itertools import groupby
from odoo.exceptions import ValidationError


class ReferralPaymentWizard(models.TransientModel):
    _name = "referral.payment.wizard"
    _description = "Referral Physician Payment"
    
    @api.onchange('date', 'physician_id')
    def _get_referral_lines(self):
        domain = [
            ('date', '<=', self.date),
            ('referral_payment_status', '=', 'pending'),
            ('physician_id', '=', self.env.context.get('active_id'))
        ]
        
        self.account_move_line_ids = self.env['account.move.line'].search(domain)
    @api.onchange( 'account_move_line_ids')
    def _compute_vendor_bill_data(self):
       
        domain = [('company_id', '=', self.env.company.id), ('type', '=', 'purchase')]
        group_account_move_line_by_currency = {k: v for k, v in groupby(
            sorted(self.account_move_line_ids, key=lambda x: x.currency_id), lambda x: x.currency_id)}
        if len(group_account_move_line_by_currency) > 1:
            raise ValidationError('Multi Currencies not supported for now')

        self.total_referral_amount =  sum(move_line.price_subtotal * move_line.product_id.categ_id.refer_percent / 100
                                         for move_line in self.account_move_line_ids)
        
    
    date = fields.Date(string='Date', default=lambda self: fields.Date.context_today(self), required=True)
   
    
   
    account_move_line_ids = fields.Many2many('account.move.line', string="Sales", compute=_get_referral_lines)
    
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, compute=_compute_vendor_bill_data)
    total_referral_amount = fields.Float(string="Total", compute=_compute_vendor_bill_data)

  


    def create_payment(self):
        
        self.check_referral_product()
        create_bill = self.env['account.move'].create(self._prepare_invoice_vals())
        for account_move_line in self.account_move_line_ids:
            account_move_line.referral_payment_status = 'done'
        
