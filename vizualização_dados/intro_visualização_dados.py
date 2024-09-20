import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\scripts\\CursoPython\\Exercicios_EBAC\\PreparaDados\\clientes-v3-preparado.csv")

print(df.head().to_string())

#----------------------------------------------- Histograma-------------------------------------------------------------
plt.hist(df['salario'])

# Histograma com Parâmetros;
plt.figure(figsize=(10, 6))
'''^^^^
Define o tamanho total do grafico;
'''
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
'''^^^^
 Define quantas colunas (bins) serão utilizadas para representar os dados (quanto mais colunas mais detalhes, porém também mais ruídos).
 Define a cor das colunas além da transparência (alpha);
'''
plt.title('Histograma - Distribuição de Salários')
'''^^^^
Define um título para o gráfico;
'''
plt.xlabel('Salario')
'''^^^^
Define a descrição para o eixo X do grafico;
'''
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
'''^^^^
Configura as marcações (ou ticks) de valores do eixo X;
ticks=range(começando de 0, até o valor máximo do campo salário + 2000, pulando de 2000 em 2000))
'''
plt.ylabel('Frequência')
'''^^^^
Define a descrição do eixo Y;
'''
plt.grid(True)
'''^^^^
Ativa as linhas de grid do gráfico;
'''
plt.show()
'''^^^^
Mostra o gráfico configurado;
'''
#------------------------------------------------------Fim Histograma---------------------------------------------------

#--------------------------------------------------Início múltiplos gráficos--------------------------------------------
# Primeiro gráfico;
plt.figure(figsize=( 10, 6)) # Define o tamanho total das caixas de exibição dos gráficos;
plt.subplot(2, 2, 1) # O campo será dividido em: 2 Linhas, 2 Colunas. Ele é o 1º Gráfico;
plt.scatter(df['salario'], df['salario']) # Define quais os campos a serem comparados;
plt.title('Dispersão - Salário e Salário') # Define o título do gráfico;
plt.xlabel('Salário') # Define a descrição do eixo X;
plt.ylabel('Salário') # Define a descrição do eixo Y;

# Segundo gráfico;
plt.subplot(1, 2, 2)
plt.scatter(df['salario'], df['idade'], color='blue', alpha=0.6, s=30)
plt.title('Dispersão de Salário por Idade')
plt.xlabel('Salário')
plt.ylabel('Idade')

# Terceiro gráfico;
corr = df[['salario', 'idade']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação entre Salário e Idade')

plt.tight_layout() # Ajusta o espaçamento entre os gráficos;
plt.show()