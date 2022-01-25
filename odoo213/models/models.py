#-*- coding: utf-8 -*-

from odoo import models, fields, api

class modelo213(models.Model):
    _name = 'odoo213.modelo213'
    _description = 'model modelo213'

    name = fields.Char('ID',required=True)
    nombre = fields.Char(string='Nombre',required=True)
    raza = fields.Char(string='Raza',required=True)

