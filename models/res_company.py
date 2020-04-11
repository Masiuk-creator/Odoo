from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    currency_rates = fields.Boolean(
        string='Currency Rates NBU/PrivatBank',
        default=True,
        help='Enable currency rates updates from NBU or PrivateBank',
        oldname='auto_currency_up'
    )


