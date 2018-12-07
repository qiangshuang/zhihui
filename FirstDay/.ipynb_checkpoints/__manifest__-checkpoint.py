# -*- coding: utf-8 -*-
{
    'name': 'FirstDay',
    'version': '12.0.1.0',
    'summary': '培训第一天',
    'author': "www.zhihui.com",
    'website': 'https://www.zhihui.com/',
    'category': 'Appiction',
    'depends': ['base'],
    'data': [
        #'security/ir.model.access.csv',
        'wizard/student_regiester_views.xml',
        'views/res_partner_views.xml',
        'views/training_lesson_views.xml',
        'views/training_subject_views.xml',
        'views/training_views.xml',
    ],
    #'demo': [
    #    'demo/pscloud_demo.xml',
    #],
    'qweb': [],
    'js': [],
    'css': [],
    'auto_install': False,
    'application': True,
}