#!/usr/bin/env python
# coding: utf-8

# # Gráficos interatívos

# Iremos neste exercício criar alguns gráficos iterativos utilizando a biblioteca python **ploty.express**.

# Inicialmente criaremos DataFrame simulado para usar como base.

# In[63]:


import pandas as pd
import numpy as np
import plotly.express as px


# In[54]:


# Criando informações a partir da biblioteca random;
idades = np.random.randint(18, 45, 20)
salarios = np.random.randint(1700, 30000, 20)
pontuacoes = salarios * np.random.uniform(0.5, 1.5, 20)

# Gerando categorias para randomizar posteriormente;
profissoes = [
    "advogado",
    "engenheiro",
    "médico",
    "programador",
    "professor",
    "cientista",
    "jornalista",
    "fazendeiro"
]
estado_civil = [
    "casado", 
    "solteiro"
]

# Criando o dict que servirá como base para nosso Dataframe;
base_dataframe = {
    "idade": idades,
    "salario": salarios,
    "pontuacoes": pontuacoes.round(2),
}
df = pd.DataFrame(base_dataframe)


# In[56]:


df["profissao"] = np.random.choice(profissoes, size=len(df))
df["estado civil"] = np.random.choice(estado_civil, size=len(df))


# In[58]:


df.head(10)


# Começaremos plotando um gráfico de barras horizontais com a média de salários por profissão:

# In[77]:


# Agrupando as informações a partir da coluna profissão e calculando o valor da média do salário de cada profissão;
media_salarios_profissao = df.groupby("profissao")["salario"].mean().reset_index()

# Gerando o gráfico de barras horizontal;
fig = px.bar(media_salarios_profissao, x="salario", y="profissao", orientation="h", # dados base, eixo_x, eixo_y, orientação das barras;
            title="Média de salários por profissão",
            labels={"salario": "Salário médio", "profissao": "Profissão"})
fig.show()


# Criando um gráfico de barras com uma legenda de calor

# In[109]:


# Agrupando as informações a partir da coluna profissão e calculando o valor da média do salário de cada profissão;
media_salarios_profissao = df.groupby("profissao")["salario"].mean().reset_index()

# Gerando o gráfico de barras horizontal;
fig = px.bar(media_salarios_profissao, x="salario", y="profissao", orientation="h",
            title="Média de salários por profissão",
            labels={"salario" : "Salário médio", "profissao" : "Profissão"},
            color="salario", # Definindo ta um mapa de cor para cada faixa de salário;
            height=450) # Definindo a altura total do gráfico;
fig.show()


# Outro visual interessante de se criar é o visual de tree map, vamos criar um exemplar para analisarmos como ele se comporta 

# In[128]:


# Agrupando os dados tanto na coluna profissão quanto na coluna estado civil;
salario_por_profissao_e_estado_civil = df.groupby(["profissao", "estado civil"])["salario"].mean().reset_index()
'''
OBS: QUANDO AGRUPAMOS AS INFORMAÇÕES EM DUAS COLUNAS, A QUANTIDADE DE REGISTROS (OU AGRUPAMENTOS) RESPEITARÁ SEMPRE O CAMPO COM MAIOR NÚMERO 
DE AGRUPAMENTOS, NESSE CASO, O CAMPO D PROFISSAO QUE POSSUI 7 AGRUPAMENTOS, ENQUANTO O CAMPO DE SALARIO POSSUI APENAS 2.
'''
fig = px.treemap(salario_por_profissao_e_estado_civil,
                path=["profissao", "estado civil"],
                values="salario",
                title="Salários por profissão",
                color="estado civil")


# In[130]:


fig.show()


# In[ ]:




