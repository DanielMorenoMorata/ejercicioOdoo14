# -*- coding: utf-8 -*-
# from odoo import http


# class Items213(http.Controller):
#     @http.route('/items213/items213/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/items213/items213/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('items213.listing', {
#             'root': '/items213/items213',
#             'objects': http.request.env['items213.items213'].search([]),
#         })

#     @http.route('/items213/items213/objects/<model("items213.items213"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('items213.object', {
#             'object': obj
#         })
