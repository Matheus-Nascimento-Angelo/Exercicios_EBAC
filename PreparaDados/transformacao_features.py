import pandas as pd
import numpy as np
from scipy import stats


pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Transformação Logarítmica;
df['salario_log'] = np.log1p(df['salario']) # utilizamos o método .log1p(porque o método log() gera problemas com valores 0, sendo assim, o método log1p() adiciona o valor 1 para evitar valores 0.
'''
Transformação logarítmica é útil para atribuirmos uma simetria maior aos dados, de modo a suavizar um
pouco a discrepância entre valores muito diferentes. Deste modo podemos trabalhar melhor com algorítmos
de machine learning, além de melhorar a visualização e interpretação dos dados em gráficos.
'''

'''
Explicação da função da escala logarítmica: A escala logarítmica diferente de uma escala linear,
os valores não são somados durante a escalada, mas sim multiplicados por uma base. Por exemplo:
Uma escala linear de base 1 de 0 a 1000 seria: "1, 2, 3, 4, 5... 1000". Já em uma escala logarítmica,
de base 10 seria: "1, 10, 100, 1000".
Mas por que usar escala logarítmica? Para podermos visualizar dados em gráficos mesmo que em proporções 
grotescamente diferentes. Por exemplo: digamos que quiséssemos plotar um grafico onde existem variáveis 
chamadas paises, e cada país possuísse o valor de sua população, um país com 1 milhão de habitantes, 
outro com 1 bilhão de habitantes. Caso usássemos uma escala linear, seria praticamente impossível
visualizar os dados do país com 1 milhão de habitantes devido a gigantesca diferença de valores, e a 
escala logarítmica resolveria isso.
'''

print(f'DataFrame após a transformação logarítmica do salário: \n{df.head()}\n')

# Transformação Box - Cox;
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1) # utilizamos o +1 para evitar valores negativos na transformação.
'''
usamos uma variável " _ " antes de atribuirmos o valor ao df["salario_boxcox"] por que o método.boxcox() retorna dois valores
o primeiro valor é o dataframe transformado contendo os valores que queremos, e o segundo valor, é o valore de "y" ou lambda
e esse valor nós não precisamos, e por convenção usamos a variável _ para descartá-lo.
'''

'''
Transformação Box Cox: oque é? É um método da biblioteca stats, que assim como o método log1p() comprime
dados em uma escala mais próxima, porém, o boxcox é mais flexível e adaptável quando comparado ao log1p
pois, o Box Cox possui internamente um parâmetro "y"(lambda) que verifica quando o valor de "y" for próximo
de 0 ou não. Quando o valor de "y" é próximo de 0, o box cox aplica automaticamente a transformação logarítmica
padrão (log1p()) porém, quando esse valor é diferente, o Box Cox verifica automaticamente, qual o melhor
método a ser aplicado, e a partir dai, executa a operação mais adequada.

Quais as diferenças entre BoxCox e log1p()? O log1p() é um método que plica a transformação logarítmica padrão
para os dados, enquanto o BoxCox verifica qual o melhor método a se seguir (multiplicação, potenciação, divisão
etc... .
Quando usar cada um? O log1p() é útil quando sabemos que nossos dados já seguem uma distribuição normal
e desejamos apenas colocar os dados em uma mesma escala.
Já o BoxCox, é útil quando desejamos além de colocar os dados em uma mesma escala, padronizá-los em uma
distribuição normal, ainda que originalmente não fossem.
'''

print(f'DataFrame após a transformação Box-Cox no salário:\n{df.head()}\n')

freq_estado = df['estado'].value_counts()/len(df) # Calculamos a frequência em porcentagem;
df['frequencia_estado'] = df['estado'].map(freq_estado) # Mapeamos os estados conforme a variável frequência em porcentagem;

print(f'DataFrame após a adição da coluna frequencia_estado:\n{df.head()}\n')

# Relação entre idade e número de filhos;
df['interacao_idade_nfilhos'] = df['idade'] * df['numero_filhos']

print(f'DataFrame após a adição da coluna "interacao_idade_nfilhos":\n{df.head()}')

df.to_csv('clientes-v2-transformados.csv', index=False)