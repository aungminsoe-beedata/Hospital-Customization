# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalCustomization(http.Controller):
#     @http.route('/hospital_customization/hospital_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_customization/hospital_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_customization.listing', {
#             'root': '/hospital_customization/hospital_customization',
#             'objects': http.request.env['hospital_customization.hospital_customization'].search([]),
#         })

#     @http.route('/hospital_customization/hospital_customization/objects/<model("hospital_customization.hospital_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_customization.object', {
#             'object': obj
#         })

