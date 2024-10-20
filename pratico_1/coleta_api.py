from bs4 import BeautifulSoup
import requests
import pandas as pd

print("Requests: ")
url = "https://br.financas.yahoo.com/quote/%5EBVSP/history/"
response = requests.get(url)
content = response.text
print("\n")

print("Beautiful Soup:")
soup = BeautifulSoup(content, "html.parser")
print("\n")

print("Pandas:")
"""
Quando passamos um url para Pandas ler, ele cria uma lista onde armazenará todas as tabelas (tags table) do documento
html, então precisamos selecionar qual tabela desejamos selecionando o elemento da lista através do seu índice.
"""
df_list = pd.read_html(url)
df = df_list[0]

print(df.head(100).to_string())