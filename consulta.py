import requests

url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"
apikey = "5EBCC73B-5DD2-43C3-BEB6-DF4BD45BC8DF"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = requests.get(url, headers=cabecera)

print(respuesta.status_code)
print(respuesta.json()["rate"])
