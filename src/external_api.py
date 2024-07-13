import os
import requests
from dotenv import load_dotenv
load_dotenv()

Apikey = os.getenv('API_KEY')
r = 'https://api.apilayer.com/exchangerates_data/convert'


def my_transactions(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях"""
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return float(transaction['operationAmount']['amount'])
    else:
        payload = {
            'amount': transaction['operationAmount']['amount'],
            'from': transaction['operationAmount']['currency']['code'],
            'to': 'RUB',
        }
        response = requests.get(str(r), headers=Apikey, params=payload)
        return response.json()['result']
