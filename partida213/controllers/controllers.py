# -*- coding: utf-8 -*-
# from odoo import http


# class Partida213(http.Controller):
#     @http.route('/partida213/partida213/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partida213/partida213/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partida213.listing', {
#             'root': '/partida213/partida213',
#             'objects': http.request.env['partida213.partida213'].search([]),
#         })

#     @http.route('/partida213/partida213/objects/<model("partida213.partida213"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partida213.object', {
#             'object': obj
#         })
