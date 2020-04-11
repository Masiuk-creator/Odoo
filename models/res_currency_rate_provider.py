import json, urllib.request


class Parser():
    def __init__(self):
        self.valuta_NBU = []
        self.valuta_PrivatBank = []

    def Get_Data_NBU(self):
        NBU = urllib.request.urlopen("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").read()
        output = json.loads(NBU)
        return output

    def Get_Data_PrivatBank(self):
        PrivatBank = urllib.request.urlopen("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").read()
        output2 = json.loads(PrivatBank)
        return output2

    def foreach_valuta_PrivatBank(self):
        for valuta in Get_Data_PrivatBank():
            if valuta['ccy'] == 'EUR':
                valuta_NBU['eur_privatbank'] = valuta['buy']
            if valuta['ccy'] == 'USD':
                valuta_NBU['usd_privatbank'] = valuta['buy']
            if valuta['ccy'] == 'RUR':
                valuta_NBU['rur_privatbank'] = valuta['buy']
        print(valuta_PrivatBank)

    def foreach_valute_NBU(self):
        for valuta in Get_Data_NBU():
            if valuta['cc'] == 'EUR':
                valuta_NBU['eur_nbu'] = valuta[rate]
            if valuta['cc'] == 'USD':
                valuta_NBU['usd_nbu'] = valuta[rate]
            if valuta['cc'] == 'RUB':
                valuta_NBU['rub_nbu'] = valuta[rate]
        print(valuta_NBU)