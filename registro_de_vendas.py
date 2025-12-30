import requests
url = 'https://app.lojaintegrada.com.br/painel/plataforma/vender'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print("Erro ao acessar API:", response.status_code)