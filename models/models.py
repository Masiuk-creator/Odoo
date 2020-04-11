# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class update_exchange_rate(models.Model):
#     _name = 'update_exchange_rate.update_exchange_rate'
#     _description = 'update_exchange_rate.update_exchange_rate'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
