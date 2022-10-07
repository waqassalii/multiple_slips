# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeliverySlips(models.Model):
    _name = 'delivery.slips'

    number = fields.Integer()
    value = fields.Char()
