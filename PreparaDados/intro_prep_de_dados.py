import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.width', None)
df = pd.read_csv('C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\materiais\\dados\\clientes-v2.csv')

# Mostrando os primeiros e últimos registros do dataframe;
print('Primeiros dez registros:')
print(df.head())

print('Últimos dez registros:')
print(df.tail())

# Reformatando o campo 'data' para date_time;
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Verificando a quantidade de dados nulos em quantidade e porcentagem;
print(f'Quantidade de dados nulos:\n{df.isnull().sum()}')
print(f'Porcentagem de dados nulos: \n{df.isnull().mean() * 100}')

# Removendo todos os dados nulos e verificando se de fato foram removidos;
df.dropna(inplace=True)
print(f'Confirmando a remoção dos dados nulos: \n{df.isnull().sum()}') # Retorna a soma de valores nulos por cada coluna do dataframe;

# Verificando se há dados duplicados;
print(f'Verificando dados duplicados:\n{df.duplicated().sum()}') # Retorna apenas um valor, representado a quantidade total de registros duplicados do dataframe;

# Verificando a quantidade de valores unicos (ou seja, campos onde o valor não existe em outros registros);
print(f'Verificando a quantidade de valores únicos:\n{df.nunique()}')

# Mostrando estatísticas dos dados;
print(f'Mostrando as estatísticas básicas dos dados:\n{df.describe()}')

# Filtrando apenas as colunas pertinentes;
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(df.head().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)

