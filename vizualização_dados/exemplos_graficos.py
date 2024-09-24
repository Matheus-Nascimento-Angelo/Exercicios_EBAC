import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.pyplot import figure

df = pd.read_csv('../PreparaDados/clientes-v3-preparado.csv')
print(df.head().to_string())
print(df.tail().to_string())

# Criando um Heatmap utilizando variáveis categóricas e quantitativas;
df_corr = df[['idade', 'mapa_estado', 'salario', 'mapa_nivel_educacao', 'numero_filhos', 'mapa_estado_civil', 'mapa_area_atuacao']].corr() # Criando a variável de correlação;
plt.figure(figsize=(10, 8)) # Configurando o tamanho da box de exibição;
sns.heatmap(df_corr, annot=True, fmt='.2f') # Criando o gráfico heatmap (dados, anotação interna: True or False, número de casas decimais da porcentagem);
plt.show()

# Criando um gráfico de distribuição de dados com agrupamento e legendas;
sns.countplot(x='estado_civil', hue='nivel_educacao' ,data=df)
plt.legend(title='Nível de educação')
plt.title('Distribuição de estado civil')
plt.xlabel('Estado civil')
plt.ylabel('Contagem')
plt.figure(figsize=(10, 8))
plt.show()
