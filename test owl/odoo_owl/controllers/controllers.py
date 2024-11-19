# -*- coding: utf-8 -*-
# from odoo import http


# class OdooOwl(http.Controller):
#     @http.route('/odoo_owl/odoo_owl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_owl/odoo_owl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_owl.listing', {
#             'root': '/odoo_owl/odoo_owl',
#             'objects': http.request.env['odoo_owl.odoo_owl'].search([]),
#         })

#     @http.route('/odoo_owl/odoo_owl/objects/<model("odoo_owl.odoo_owl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_owl.object', {
#             'object': obj
#         })

