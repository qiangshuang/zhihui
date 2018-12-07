# -*- coding: utf-8 -*-

from odoo import api, fields, models
import datetime

class Lession(models.Model):
    _name = 'zhihui.lesson'
    _description = "课程信息"

    name = fields.Char(string='Name')
    teacher_id = fields.Many2one('res.partner', string='老师', domain=[('is_teacher', '=', True)])
    student_ids = fields.Many2many('res.partner', string='学生', domain=[('is_student', '=', True)], readonly=True)
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')
    
    
    seat_qty = fields.Integer(string='座位数')
    subject_id = fields.Many2one('subject', string='科目')
    person_id = fields.Many2one('res.partner', related='subject_id.person_id', readonly=True)
    desc = fields.Text(string='描述')