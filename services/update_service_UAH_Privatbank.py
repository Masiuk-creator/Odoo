import datetime
import requests

from xmltodict import parse

from odoo.addons.currency_rate_update import CurrencyGetterInterface


class UAH_NBU_getter(CurrencyGetterInterface):
    code = "UAH_PrivatBank"
    name = "UAH PrivatBank Currency Rates"

    supported_currency_array = [
        "USD", "EUR", "RUR"]

    def get_updated_currency(self, currency_array, main_currency, date_req=None):
        """implementation of abstract method of Currency_getter_interface"""

        params = {}
        if date_req:
            params['date_req'] = date_req
        else:
            # always set day, CB set rate from yesterday to tommorow
            params['date_req'] = datetime.date.today().strftime('%d/%m/%Y')
        response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11',
                                params=params)
        response.encoding = 'cp1251'
        rates = {}
        text = response.text.encode('utf-8').replace('windows-1251', 'utf-8')
        privatbank = parse(text)
        for valute in privatbank['exchangerates']['row']:
            valute['row'] = float(valute['row'].replace(',', '.'))
            rates[valute['buy']] = valute['row']

        if main_currency in currency_array:
            currency_array.remove(main_currency)
        main_currency_data = 1
        if main_currency != 'UAH' and main_currency:
            main_currency_data = rates[main_currency]
            rates['UAH'] = 1

        for curr in currency_array:
            self.validate_cur(curr)
            self.updated_currency[curr] = main_currency_data / rates[curr]

        return self.updated_currency, self.log_info