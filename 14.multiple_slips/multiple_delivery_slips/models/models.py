# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    delivery_slip = fields.Integer(default_model='stock.picking', string="No. of Delivery Slip", default=1)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = (self.env['ir.config_parameter'].sudo())
        res.update(
            delivery_slip=int(ICPSudo.get_param('multiple_delivery_slips.delivery_slip')),
        )

        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        if self.delivery_slip:
            self.env['ir.config_parameter'].sudo().set_param('multiple_delivery_slips.delivery_slip',
                                                             self.delivery_slip)
        return res


class StockInherit(models.Model):
    _inherit = 'stock.picking'

    def get_num_of_slips(self):
        partner_delivery = self.env['ir.config_parameter'].sudo().get_param(
            'multiple_delivery_slips.delivery_slip') or False
        return int(partner_delivery)

    def get_num_text(self, num):
        if num:
            val = self.env['delivery.slips'].search([('number', '=', num)])
            if val:
                return val.value
