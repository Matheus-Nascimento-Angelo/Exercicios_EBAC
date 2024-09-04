import requests
from bs4 import BeautifulSoup
import pandas as pd

  # Carrega o HTML na variável response como uma única linha;
response = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history/')
print('Response:')
print(response.text[:1000])

  # Estrutura os dados com indentação html;
soup = BeautifulSoup(response.text, 'html.parser')
print('BeautifulSoup:')
print(soup.prettify()[:1000])

  # Carregar e transformar os dados HTML em um DataSet através do pandas;
url_dados = pd.read_html('https://br.financas.yahoo.com/quote/%5EBVSP/history/') # Retorna uma lista de DataFrames;
print('Pandas:')
print(url_dados[0].head(10))