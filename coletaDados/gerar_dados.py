import pandas as pd
from faker import Faker
import random

faker = Faker('pt-br')

def gera_dados():
    dados_pessoas = []

    for _ in range(1000):
        nome = faker.name() if random.random() > 0.08 else None
        cpf = faker.cpf() if random.random() > 0.08 else None
        idade = random.randint(5, 19)
        data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y') if random.random() > 0.08 else None
        endereco = faker.address() if random.random() > 0.08 else None
        estado = faker.state() if random.random() > 0.08 else None
        pais = 'Brasil'

        pessoa = {'nome':nome,
                  'cpf':cpf,
                  'idade':idade,
                  'data_de_nascimento':data,
                  'endereco':endereco,
                  'estado':estado,
                  'pais':pais}

        dados_pessoas.append(pessoa)
    return dados_pessoas

df_pessoas = pd.DataFrame(gera_dados())

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(df_pessoas.to_string())

df_pessoas.to_csv('Cliente_csv', index=False)