from odoo import api, fields, models


class ResConfigSettingsRatesProvider(models.TransientModel):
    _inherit='res.config.settings'

    nbu_provider=fields.Many2one(
        'nbu.rates',
        'NBU provider',
        help = 'Exchange rates from NBU'
    )

    privatbank_provider = fields.Many2one(
        'privatbank.rates',
        'PrivatBank provider',
        help='Exchange rates from PrivatBank'
    )
    @api.model
    def get_values(self):
        res=super(ResConfigSettingsRatesProvider, self).get_values()
        res.update(
            nbu_provider=int(self.env['ir.config_parameter'].sudo().get_param('rates_update.nbu_provider')),
            privatbank_provider = int(self.env['ir.config_parameter'].sudo().get_param('rates_update.privatbank_provider')),
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettingsRatesProvider, self).set_values()
        if self.nbu_provider:
            self.env['ir.config_parameter'].sudo().set_param('rates_update.nbu_provider',
                                                             repr(self.nbu_provider.id))
        if self.privatbank_provider:
            self.env['ir.config_parameter'].sudo().set_param('rates_update.privatbank_provider',
                                                             repr(self.privatbank_provider.id))