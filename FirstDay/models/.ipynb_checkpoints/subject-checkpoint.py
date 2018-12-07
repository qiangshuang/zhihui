# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Subject(models.Model):
    _name = 'zhihui.subject'
    _description = "科目"

    name = fields.Char(string='名称')
    person_id = fields.Many2one('res.partner', string='负责人')
    lesson_ids = fields.One2many('zhihui.lesson', 'subject_id', string='课程')
    desc = fields.Text(string='描述')