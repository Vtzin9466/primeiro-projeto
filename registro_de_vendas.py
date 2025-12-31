import requests
url = 'https://api.skubana.com/'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print("Erro ao acessar API:", response.status_code)