import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\scripts\\CursoPython\\Exercicios_EBAC\\PreparaDados\\clientes-v3-preparado.csv")

print(df.head().to_string())

#--------------------------- gráfico de barras
# Plotando gráfico de barras configurando o parâmetro 'kind';
plt.figure(figsize=(10, 6)) # Configura o tamanho da box que exibirá o gráfico;
df['nivel_educacao'].value_counts().plot(kind='bar', color='blue')
plt.show()

# Plotando gráfico de barras a partir do método específico plt.bar() para gráfico de barras;
x = df['nivel_educacao'].value_counts().index # Acessa os indexes do dataframe na coluna nivel_educacao;
y = df['nivel_educacao'].value_counts() # Acessa os valores do dataframe na coluna nivel_educacao;

plt.figure(figsize=(10, 6)) # Configura o tamanho da box que exibirá o gráfico;
plt.bar(x, y, color='green')  # Informa os valores que deverão estar presentes nos eixos x e y do gráfico, além de configurar a cor das barras
plt.show()

#--------------------------- gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90, ) # .pie(valores, categorias, número de casas decimais, angulo inicial do gráfico)
plt.title('Distribuição do nível de educação')
plt.show()

#-------------------------- gráfico de dispersão (ou correlação)
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

