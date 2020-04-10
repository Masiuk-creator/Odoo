import json,urllib.request

NBU = urllib.request.urlopen("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").read()
output = json.loads(NBU)
z=output[0:58]
print (z)


PrivatBank = urllib.request.urlopen("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").read()
output2 = json.loads(PrivatBank)
k=output2[0:3]
print (k)
