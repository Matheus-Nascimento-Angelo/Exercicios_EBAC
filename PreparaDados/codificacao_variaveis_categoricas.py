import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)
df = pd.read_csv('clientes-v2-tratados.csv')

# 1 método: Codificando one-hot para 'estado_civil';
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
'''^^^^ Primeiro objetô(df) | Segundo objeto (colunas geradas ^ pelo método get_dummies( )) ^ eixo de concatenação (axis=1 concatena na dimensão das colunas)
Concatena o dataframe "df" com as categóricas binárias geradas a partir do método "get_dummies( )".
método "get_dummies( )": parâmetros: (data, prefixo, prefixo separador(opc), categoria para nulos(opc), 
descartar primeira categoria(opc). data = df base ou data set, prefixo = prefixo anterior a categoria, prefixo separador(opc) = prefixo separador
entre o prefixo e categoria, coluna para nulos(opc) = categoria que conterá a quantidade de valores nulos.
'''
print(f'\n1 MÉTODO: DataFrame após a codificação one-hot para "estado_civil": \n{df.head()}')

# método> Codificação ordinal para 'estado_civil';
mapa_estado_civil = {'Casado':1, 'Solteiro':2, 'Divorciado':3, 'Viúvo':4}
df['mapa_estado_civil'] = df['estado_civil'].map(mapa_estado_civil)

# 2 método: Codificação ordinal para "nivel_educacao" (definindo valores numéricos para cada registro único do campo);
mapa_nivel_educacao = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['mapa_nivel_educacao'] = df['nivel_educacao'].map(mapa_nivel_educacao) # Mapeando as variáveis quali a partir do mapa(dicionario) criado anteriormente;
'''^^^^
criamos uma nova coluna chamada nivel_educacao_ordinal que receberá o resultado do mapeamento das categorias a partir da variável mapa_nivel_educacao
(um dicionário contendo como chaves os nomes de cada valor único presentes na coluna nivel_educacional do data frame df) criada por nós mesmos.
'''
print(f'\n2 MÉTODO: DataFrame após codificação ordinal para "nivel_educacao":\n {df.head()}\n')

# 3 método cat.codes;
df['mapa_area_atuacao'] = df['area_atuacao'].astype('category').cat.codes
print(f'3 MÉTODO: DataFrame após transformar "area_atuacao" em códigos numéricos:\n {df.head()}\n')
'''
criamos uma nova coluna no dataframe chamada "mapa_area_atuacao" atribuímos a ela o resultado do processo de transformação dos valores da coluna original em
tipo "category", dados desse tipo, são extremamente úteis pois fornecem "um campo para etiquetar os registros", após isso, o atributo "cat.codes" atribui a esse
"campo para etiquetar registros" os valores de registros presentes nos atributos;
'''

# 4 método: Label Encoder;
Label_encoder = LabelEncoder()
df['mapa_estado'] = Label_encoder.fit_transform(df['estado'])
print(f'4 MÉTODO: DataFrame após aplicar o LabelEncoder em "estado": \n{df.head()}')

'''
Método fit_transform(): fit = aprende ou se ajusta as categorias (valores únicos) presentes na coluna 'estado'.
tranform = converte cada categoria aprendida no fit em um número inteiro com base em uma ordenação alfabética;
após isso atribui a coluna 'mapa_estado' os resultados obtidos no transform;
'''
df.to_csv("clientes-v3-preparado.csv", index=False)
