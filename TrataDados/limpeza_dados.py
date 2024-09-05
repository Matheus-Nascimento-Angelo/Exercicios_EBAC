import pandas as pd

# Carregando o DataFrame;
df = pd.read_csv('C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\materiais\\dados\\clientes')

print(df.columns)
pd.set_option('display.width', None)

# Remover dados;
df.drop('pais', axis=1, inplace=True) # Removendo a coluna pais;
df.drop(2, axis=0, inplace=True) # Removendo a 3 linha;

# Normalizar campos de texto;
df['estado'] =  df['estado'].str.lower()
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()

# Converter tipo de dados;
df['idade'] = df['idade'].astype(int)

# Tratar valores nulos;
df_fillna = df.fillna(0) # Substitui nulos;
df_dropna = df.dropna() # Remove valores nulos;
df_dropna4 = df.dropna(thresh=4) # Remove a linha ou coluna, caso tenha mais de 4 valores nulos;
df = df.dropna(subset='cpf') # Remove os registros com valores nulos na coluna cpf apenas;

# Mostrando a ação dos diferentes tratamentos para valores nulos;
print(f'Valores nulos: \n{df.isnull().sum().sum()}')
print(f'Qnt de registros nulos com fillna(): \n{df_fillna.isnull().sum().sum()}')
print(f'Qnt de registros nulos com dropna(): \n{df_dropna.isnull().sum().sum()}')
print(f'Qnt de registros nulos com dropna(thresh=4): \n{df_dropna4.isnull().sum().sum()}')
print(f'Qnt de registros com o campo cpf com valores nulos: \n{df.isnull().sum().sum()}')

# Substituindo campos nulos com valores personalizados;
df.fillna({'estado': 'Desconhecido'}, inplace=True) # Substitui valores nulos no campo 'estado' para 'desconhecido';
df['endereco'] = df['endereco'].fillna('Endereço não informado') # Substitui valores nulos no campo 'endereco' para 'Endereço não informado';
df['idade'] = df['idade'].fillna(df['idade'].mean()) # Substitui valores nulos no campo 'idade' pela média do campo idade;

# Tratar formato dos dados;
df['data'] = pd.to_datetime(df['data_de_nascimento'], format='%d/%m/%Y', errors='coerce')

# Tratar dados duplicados;
print(f'Qnt de registros atual: \n{df.shape[0]}')
#df = df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print(f'Qnt de registro removendo as duplicatas: \n{len(df)}')

print(f'Dados limpos:\n{df.to_string()}')

# Cria um novo Dataframe filtrando apenas as colunas desejadas;
df_salva = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]

# Exporta o DataFrame como um arquivo csv;
df_salva.to_csv('clientes_limpeza.csv', index=False) # index=False serve para não criar uma nova coluna de índice no novo dataframe;

print(pd.read_csv('clientes_limpeza.csv'))