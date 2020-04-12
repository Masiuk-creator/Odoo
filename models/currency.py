import datetime
import logging
import socket
import os

from odoo import _, api, models, fields, exceptions
from odoo.tools.translate import _

# from ..services.currency_getter import Currency_getter_factory
from ..services.update_service_UAH_NBU import UAH_NBU_getter

_logger = logging.getLogger(__name__)
CURRENCY_DOMAIN = [('name', 'in', ['RUB', 'USD', 'EUR'])]


class Currency(models.Model):
    _inherit = 'res.currency'

    uah_currency_rate = fields.Float(string=u"Rate",
                                     compute='compute_uah_currency',
                                     digits=(12, 4),
                                     )

    rate_moment = fields.Selection(string=u"Moment",
                                  selection='get_rate_moment_selection',
                                  compute='compute_rate_moment_selection',
                                  )
    cron1_currency_update_id = self.env.ref('currency_rate_update.ir_cron_currency_update_every_minute')

    rate_hour = fields.Selection(string=u"Hour",
                                  selection='get_rate_hour_selection',
                                  compute='compute_rate_hour_selection',
                                  )
    cron2_currency_update_id = self.env.ref('currency_rate_update.ir_cron_currency_update_every_hour')

    rate_day = fields.Selection(string=u"Day",
                                  selection='get_rate_day_selection',
                                  compute='compute_rate_day_selection',
                                  )
    cron3_currency_update_id = self.env.ref('currency_rate_update.ir_cron_currency_update_every_day')

    rate_week = fields.Selection(string=u"Week",
                                  selection='get_rate_week_selection',
                                  compute='compute_rate_week_selection',
                                  )
    cron4_currency_update_id = self.env.ref('currency_rate_update.ir_cron_currency_update_every_week')

    rate_month = fields.Selection(string=u"Month",
                                  selection='get_rate_month_selection',
                                  compute='compute_rate_month_selection',
                                  )
    cron5_currency_update_id = self.env.ref('currency_rate_update.ir_cron_currency_update_every_month')

    force_refresh = fields.Boolean(string=u'Forced')

    @property
    def uah_id(self):
        return self.env.ref('base.UAH')

    @property
    def eur_id(self):
        return self.env.ref('base.EUR')

    @property
    def usd_id(self):
        return self.env.ref('base.USD')

    @api.v8
    def compute_uah(self, from_amount, round=True):
        return self.compute(from_amount, self.uah_id, round)

    @api.v8
    def compute_eur(self, from_amount, round=True):
        return self.compute(from_amount, self.eur_id, round)

    @api.v8
    def compute_usd(self, from_amount, round=True):
        return self.compute(from_amount, self.usd_id, round)

    @api.multi
    def compute_uah_currency(self):
        for rec in self:
            if uah.rate:
                rec.uah_currency_rate = 1. / rec.rate

    today = datetime.date.today()
    date = fields.Date.from_string(self.from_date)
    if self.force_refresh:
        rec_dates = set()
    else:
        rec_dates = set(self.env['res.currency.rate'].search(
            [('currency_id', '=', self.id),
             ('name', '>=', fields.Datetime.to_string(date))]).mapped('name'))

    class Rate(models.Model):
        _inherit = "res.currency.rate"

        uah_currency_rate = fields.Float(string=u"Rate",
                                         compute='compute_uah_currency',
                                         digits=(12, 4),
                                         )