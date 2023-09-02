#Fazer GET na API
import pandas as pd
import requests as req

url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$format=json'
response = req.get(url)
json_data = response.json()

# Tratar os dados

currency_data = json_data.get('value', [])
df = pd.DataFrame(currency_data)
print(df)

#Salvar em Excel
excel_file = 'Moedas.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')