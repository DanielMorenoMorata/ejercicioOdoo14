#-*- coding: utf-8 -*-

from odoo import models, fields, api

class objetos213(models.Model):
 _name = 'items213.objetos213'
 _description = 'model objetos213'

 name = fields.Char('ID',required=True)
 nombre = fields.Char(string='Nombre',required=True)
 cantidad = fields.Char(string='cantidad',required=True)

