import pandas as pd

df = pd.read_csv('C:/Users/mathe/Documents/estudos/data-science/Cientista_de_dados-EBAC/materiais/dados/clientes.csv')

# Mostra os primeiros registros;
print(f'Primeiros registros: \n{df.head().to_string()}\n')

# Mostra os últimos registros;
print(f'Últimos registros: \n{df.tail().to_string()}\n')

# Mostra a quantidade de linhas e colunas;
print(f'Formato do Data Frame: \n{df.shape}\n')

# Mostra o tipo dos dados;
print(f'Tipagem: \n{df.dtypes}\n')

# Checa os valores nulos;
print(f'Valores nulos: \n{df.isnull().sum()}')