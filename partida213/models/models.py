#-*- coding: utf-8 -*-

from odoo import models, fields, api

class pta213(models.Model):
    _name = 'partida213.pta213'
    _description = 'model pta213'

    name = fields.Char('ID',required=True)
    sistema = fields.Char(string='Sistema',required=True)
    jugadores = fields.Char(string='Jugadores',required=True)

