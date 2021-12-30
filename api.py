import requests
import json 

currentQuote = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

valueQuote = currentQuote.json()

USDBRL = valueQuote['USDBRL']['bid']
EURBRL = valueQuote['USDBRL']['bid']
BTCBRL = valueQuote['BTCBRL']['bid']

print(f'Cotação: Dólar Americano/Real Brasileiro => {USDBRL}')
print(f'Cotação: Euro/Real Brasileiro => {EURBRL}')
print(f'Cotação: Bitcoin/Real Brasileiro => {BTCBRL}')
