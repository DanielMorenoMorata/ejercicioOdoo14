#-*- coding: utf-8 -*-
from openerp import models, fields

class App01Task(models.Model):
    _name = 'app01.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
