import requests

def convert_currency(amount, from_currency, to_currency):
    url = f""https://api.exchangerate-api.com/v4/latest/{from_currency}""
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return amount * rate

amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
