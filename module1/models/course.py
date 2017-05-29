
# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Course(models.Model):
    _name = 'openacademy.course'
    _inherit = 'mail.thread'
    
    name = fields.Char(name='Title', required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible")
    level = fields.Selection([('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], string="Difficulty Level")
    
