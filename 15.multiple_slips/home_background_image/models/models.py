# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    dashboard_background_img = fields.Binary(attachment=True,string="Dashboard background")


