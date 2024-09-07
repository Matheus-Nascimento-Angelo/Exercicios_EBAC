from selectors import SelectSelector

import pandas as pd
import numpy as np
from django.utils.http import escape_leading_slashes

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\materiais\\dados\\clientes_remove_outliers.csv')

# Aplicando mascaras em campos com dados sensíveis, como o cpf;
df['cpf_mascara'] =  df['cpf'].apply(lambda cpf: f'{cpf[0:3]}.***.*** - {cpf[-2:]}')

# Corrigindo o campo de datas;
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

# Verificando se a data de nascimento é válida (se é uma data anterior a data atual);
data_de_hoje = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_de_hoje, pd.to_datetime('01-01-1800'))
'''^^^^^^
df[data_atualizada] recebe o valor de df[data] onde o valor de df[data] for menor que a data de hoje, 
se não, aplica ao campo df[data] a data de 01/01/1800
'''

df['idade_ajustada'] = data_de_hoje.year - df['data_atualizada'].dt.year # Atualiza a idade pegando o valor do campo do ano atual e subtraindo pelo campo do ano da data atual da variável
df['idade_ajustada'] =- ((data_de_hoje.month <= df['data_atualizada'].dt.month) & (data_de_hoje.day < df['data_atualizada'].dt.day)).astype(int)
'''^^^^^^
Verifica se a data de aniversário de cada registro ja passou ou não.
realiza um teste lógico que retornará um booleano convertido para inteiro que será subtraído da idade caso seja verdadeiro: 
idade -= ((mes atual menor ou igual ao mes de aniversário) e (dia atual menor que o dia do aniversário)) transforme para o 
tipo inteiro (1 para True, ou 0 para False). Ao fim se subtrai o valor retornado da idade, caso seja False a idade se mantem a mesma
porém caso seja True, será subtraído -1 do campo idade do registro.
'''

df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan # Se a idade for maior que 100, atribua o valor nan ao campo;
'''^^^^^^
OBS: Diferenças entre os atributos .loc e .iloc é que o .loc seleciona campos específicos com base ou em seus nomes, ou seus valores ou condições lógicas
enquanto o atributo .iloc seleciona os campos a partir dos seus indexes de posição. O atributo loc seleciona tanto o limite inferior quanto o superior 
do filtro, enquanto o iloc utiliza o mesmo sistema tradicional do python, não selecionando o limite superior do filtro.
'''

# Corrigir campos com múltiplas informações;
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
'''^^^^^^
a função apply() sempre deve ser chamada quando desejamos realizar tratamentos internos em um campo do dataframe, pois ela é quem aplica os tratamentos
aos campos depois que todo o processo é feito.
'''
df['rua'] = df['endereco_curto'].apply(lambda x: x.split(',')[0].strip() if ',' in x else x) # Seleciono apenas os caracteres referentes ao nome da rua;
df = df.drop('endereco_curto', axis=1)

df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split('/')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
# Verifica se o tamanho do campo endereço é aceitável;
df['endereco'] = df['endereco'].apply(lambda x: 'Desconhecido' if len(x) < 10 or len(x) > 70 else x)

'''
Sintaxe de expressões ternárias: em expressões ternárias, diferente de declarações condicionais comuns, nós atribuímos o resultado final a variável antes
de realizar a validação lógica da operação, e só após demonstrarmos o valor a ser atribuído em caso de um retorno positívo é que realizamos a operação
lógica em sí. Exemplo: lambda x: (apresenta o valor a ser atribuído)->'x_maior' (define o teste lógico a ser realizado)-> if x > 5 (declara o valor a ser aplicado em caso de resultado negativo) -> else x
'''

# Verifica se quantidade de dígitos do campo cpf está correta;
df['cpf'] = df['cpf'].apply(lambda x: 'CPF inválido' if len(x) != 14 else x)

# Verifica se os valores do campo estado de fato são siglas dos estados brasileiros;
siglas_estado = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
df['estado_sigla'] = df['estado_sigla'].str.strip().str.upper().apply(lambda x: x if x in siglas_estado else 'Desconhecido')

# Renomeia as colunas do dataframe;
df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco']
df['estado'] = df['estado_sigla']

# Exporta o dataframe em um arquivo csv;
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)
