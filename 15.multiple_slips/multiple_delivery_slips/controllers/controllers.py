# -*- coding: utf-8 -*-
# from odoo import http


# class MultipleDeliverySlips(http.Controller):
#     @http.route('/multiple_delivery_slips/multiple_delivery_slips', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multiple_delivery_slips/multiple_delivery_slips/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('multiple_delivery_slips.listing', {
#             'root': '/multiple_delivery_slips/multiple_delivery_slips',
#             'objects': http.request.env['multiple_delivery_slips.multiple_delivery_slips'].search([]),
#         })

#     @http.route('/multiple_delivery_slips/multiple_delivery_slips/objects/<model("multiple_delivery_slips.multiple_delivery_slips"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multiple_delivery_slips.object', {
#             'object': obj
#         })
