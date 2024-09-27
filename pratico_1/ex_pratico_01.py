import pandas as pd
from scipy.stats import alpha
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', '{:.2f}'.format)

df = pd.read_csv('ecommerce_preparados.csv')

print(df.head().to_string())
print(df.tail().to_string())

# Verificando a quantidade de dados nulos;
print('\nDados nulos:')
print(df.isnull().sum())

# Removendo campos indesejados;
df = df.drop(['Review1', 'Review2', 'Review3', 'Unnamed: 0'], axis=1)

# Tratando valores nulos;
'''
Substituindo valores nulos de variáveis quantitativas por 0 para evitar possíveis problemas
caso precisemos realizar algum processo matemático utilizando esses campos ( como vai ser o caso );
'''
df['Nota'] = df['Nota'].fillna(0)
df['N_Avaliações'] = df['N_Avaliações'].fillna(0)
df['Desconto'] = df['Desconto'].fillna(0)
df['Preço'] = df['Preço'].fillna(df['Preço'].mean())

# Tratando valores nulos de variáveis qualitativas;
df['Material'] = df['Material'].fillna('Pendente')
df['Gênero'] = df['Gênero'].fillna('Pendente')

'''
Criando novas variáveis normalizadas após o tratamento dos valores nulos presentes nos dados originais;
'''
minmax_scaler = MinMaxScaler()
df['Nota_MinMax'] = minmax_scaler.fit_transform(df[['Nota']])
df['N_Avaliações_MinMax'] = minmax_scaler.fit_transform(df[['N_Avaliações']])
df['Desconto_MinMax'] = minmax_scaler.fit_transform(df[['Desconto']])
df['Preço_MinMax'] = minmax_scaler.fit_transform(df[['Preço']])

'''
Criando novas variáveis categóricas após o tratamento dos valores nulos presentes nos dados originais;
'''
mapa_quantidade_vendidos = {'+5':5 ,'+25':25, '+50':50, '+100':100, '+1000':1000,'+5mil':5000 ,'+10mil':10000, '+50mil':50000}
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(mapa_quantidade_vendidos)
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos_Cod'].fillna(0)
df['Cod_Titulo'] = df['Título'].astype('category').cat.codes
'''
Criando mapas de frequência após o tratamento dos valores nulos presentes nos dados originais;
'''
freq_material =df['Material'].value_counts()/len(df)
df['Material_Freq'] =df['Material'].map(freq_material)

print('\nDados após o tratamento\n')
print(df.head(100).to_string())

# Início da visualização dos dados;

# Gráfico de dispersão;
sns.jointplot(x='Nota', y='N_Avaliações', data=df, kind='scatter', alpha=0.5)
plt.xlabel('Nota')
plt.ylabel('Número de avaliações')
plt.show()

# Gráfico de calor (heatmap);
corr = df[['Qtd_Vendidos_Cod', 'N_Avaliações', 'Material_Cod', 'Temporada_Cod']].corr()
x_axis = ['Quantidades vendidas', 'Número de avaliações', 'Material', 'Temporada']
sns.heatmap(corr, xticklabels=x_axis, yticklabels=x_axis,annot=True, cmap='coolwarm')
plt.title('Correlação entre variáveis')
plt.show()

# Gráfico de barras;
plt.figure(figsize=(10, 6))
df['Material'][0:11].value_counts().plot(kind='bar', color='blue')
plt.title('Distribuição dos dados no campo Material')
plt.xlabel('Materiais')
plt.ylabel('Total de aparições')
plt.show()

# Gráfico de pizza;

y = df['Marca'][:11].value_counts()
x = df['Marca'][:11].value_counts().index

plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição do campo Marcas, em porcentagem')
plt.show()

# Gráfico de densidade;
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='red')
plt.title('Densidade do campo Preços')
plt.xlabel('Preços')
plt.show()
