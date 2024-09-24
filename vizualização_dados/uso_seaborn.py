import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../PreparaDados/clientes-v3-preparado.csv')
print(df.head().to_string())
print(df.tail().to_string())

# Gráfico de dispersão;
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') # tipos de gráficos: scatter - dispersão, hist - histograma, hex, kde, resid.
plt.show()
'''
diferentemente dos gráficos plotados utilizando o matplotlib, os dados que são utilizando para a montagem dos gráficos
do seaborn são declarados dentro da própria função geradora dos gráficos, sendo passados como argumento para o método.
'''
# Gráfico de densidade (histograma com suavização nas curvas);
plt.figure(figsize=(6, 10))
sns.kdeplot(df['salario'], fill=True, color='Blue')
plt.title('Gráfico de densidade')
plt.xlabel('salário')
plt.show()

# Gráfico de PairPlot (densidade e histograma) utilizando múltiplas variáveis;
sns.pairplot(df[['idade', 'salario', 'numero_filhos', 'nivel_educacao']])
plt.show()

# Gráfico de regressão;
sns.regplot(x='idade', y='salario', data=df, color='Pink', scatter_kws={'alpha':0.5, 'color':'Red'})
plt.title('Gráfico de regressão')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico de countplot com hue (agrupamento);
sns.countplot(x='nivel_educacao', hue='estado_civil', data=df, palette='pastel')
plt.xlabel('Estado civil')
plt.ylabel('Nível de educação')
plt.legend(title='Nível de educação')
plt.show()
