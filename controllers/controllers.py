# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateExchangeRate(http.Controller):
#     @http.route('/update_exchange_rate/update_exchange_rate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_exchange_rate/update_exchange_rate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_exchange_rate.listing', {
#             'root': '/update_exchange_rate/update_exchange_rate',
#             'objects': http.request.env['update_exchange_rate.update_exchange_rate'].search([]),
#         })

#     @http.route('/update_exchange_rate/update_exchange_rate/objects/<model("update_exchange_rate.update_exchange_rate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_exchange_rate.object', {
#             'object': obj
#         })
