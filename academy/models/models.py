# -*- coding: utf-8 -*-

from odoo import models, fields, api


class academy(models.Model):
     _name = 'academy.academy'
     _description = 'academy.academy'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
     course_id = fields.Many2one('academy.courses')

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100


class courses(models.Model):
    _name = 'academy.courses'
    _description = "Model for academy courses"

    name = fields.Char(string="Name")
    academy_id = fields.Many2one('academy.academy')
    academy_many = fields.Many2many('academy.academy')
    academy_one = fields.One2many('academy.academy', 'course_id', string="Academy Model")
