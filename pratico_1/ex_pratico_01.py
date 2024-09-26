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
sns.jointplot(x='Nota', y='N_Avaliações', data=df, kind='scatter', alpha=0.5)
plt.show()

corr = df[['Qtd_Vendidos_Cod', 'N_Avaliações', 'Material_Cod', 'Temporada_Cod']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()




