import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\materiais\\dados\\clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100] # Atribui a variável os registros em que o campo 'idade' é maior que 100;

print(f'Filtro básico: \n{df_filtro_basico[['nome', 'idade']]}')

# Identificar outliers com o Z-score;
z_scores = stats.zscore(df['idade']) # Calcula quantos desvios padrão os valores de um campo estão de distância da média;
outliers_z = df[z_scores >= 3] # A variável recebe apenas os registros em que o campo 'idade' está a pelo menos 3 desvios padrão de distância da média;
print(f'Outliers pelo Z-score:\n{outliers_z}')

# Filtrar apenas os valores com Z-score menor que 3 desvios padrão de distância da média;
df_zscore = df[(stats.zscore(df['idade'])) < 3]

'''          ^^^^^^^^ Explicação da linha a cima ^^^^^^^^

A expressão stats.zscore() < 3 retorna um array booleano, de True e False, após realizar
a operação declarada, então esse array boobleano serve como filtro ou mascara para 
selecionar apenas os registros que correspondem oa valor True da mascara boobleana,
descartando os valores do dataframe correspondentes ao valor False da mascara.
'''
'''OBS: a expressão (stats.zscore(df['idade']) deve estar entre parenteses graças a ordem de
precedência, ou seja, para garantir que o calculo do zscore ocorra antes da comparação entre
o z-score e o número 3'''

# Identificar outliers com IQR;
Q1 = df['idade'].quantile(0.25) # Q1 recebe valor referente ao primeiro quartil do dataframe;
Q3 = df['idade'].quantile(0.75) # Q3 recebe o valore referente ao terceiro quartil do dataframe;
IQR = Q3 - Q1 # Medida da amplitude dos 50% valores centrais de um conjunto de dados;

# Estes cálculos tratam de uma fórmula, sempre utilizada nesse mesmo padrão para definir os limites superiores e inferiores, o valor 1.5 trata-se de um valor de convenção geral;
limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)] # Selecionando os valores Outliers;
''' ^     ^^^^^^^^^^^^^Explicação da linha a cima ^^^^^^^^^^^^^^

Primeiro referenciamos o data frame 'df', abrimos colchetes indicando que selecionaremos apenas partes específicas do
data frame, dentro dos colchetes, abrimos parentes para isolarmos a primeira operação lógica, que é:
(se o valor do campo df['idade'] estiver a baixo do limite_baixo: retorne True) ou se (| realiza a operação lógica "ou")
(o valor do campo df['idade'] estiver a cima do limite_alto: também retorne True)
como resultado dessa operação lógica, será retornado um array de booleanos, esse array será utilizado como máscara para
selecionar apenas os campos correspondentes aos valores True do array de booleanos, os campos que corresponderem ao valor
False são descartados do data frame, como resultado a variável outliers_iqr armazenará apenas valores outliers.
'''
print(f'Outliers IQR:\n{outliers_iqr.to_string()}')

# Remover outliers via IQR;
df_iqr = df[(df['idade'] <= limite_alto) | (df['idade'] >= limite_baixo)]

# Filtrar endereços inválidos;
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)
'''
Aplica uma função lambda e atribui o texto 'Endereço inválido' ao campo endereço se o comprimento do valor quando dividido no caractere \n
for maior que 3.
'''
print(df['endereco'])

# Filtrar nomes inválidos;
df['nome'] = df['nome'].apply(lambda x: 'Nome muito grande' if isinstance(x, str) and len(x) > 30 else x) # isinstance(variável, tipo) verifica se o tipo da variável e do tipo de dado desejado
print(f'Quantidade de nomes grandes: {(df['nome'] == 'Nome muito grande').sum()}')

df.to_csv('clientes_remove_outliers.csv', index=False)