# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo213(http.Controller):
#     @http.route('/odoo213/odoo213/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo213/odoo213/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo213.listing', {
#             'root': '/odoo213/odoo213',
#             'objects': http.request.env['odoo213.odoo213'].search([]),
#         })

#     @http.route('/odoo213/odoo213/objects/<model("odoo213.odoo213"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo213.object', {
#             'object': obj
#         })
