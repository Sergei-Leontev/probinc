import requests
import json
class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Ошибка.невозможно перевести одни и теже валюты{base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Ошибка.не удолось оброботать валюту{quote}")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Ошибка.не удолось оброботать валюту{base}")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Ошибка.не удолось оброботать количество{amount}")
        r = requests.get(f'https: //min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base

