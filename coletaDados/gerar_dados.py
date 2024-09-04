import pandas as pd
from faker import Faker
import random

faker = Faker('pt-br')

def gera_dados():
    dados_pessoas = []

    for _ in range(10):
        nome = faker.name()
        cpf = faker.cpf()
        idade = random.randint(5, 19)
        data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
        endereco = faker.address()
        estado = faker.state()
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

df_pessoas.to_csv('Cliente_csv')