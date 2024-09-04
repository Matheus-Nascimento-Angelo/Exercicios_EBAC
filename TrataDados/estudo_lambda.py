import pandas as pd

# Função calcular o cubo de um número;
def eleva_ao_cubo(x):
    return x ** 3

# Expressão de lambda para calcular o cubo de um número;
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_ao_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'Números': [1, 2 , 3, 4, 5, 10]})

df['cubo_funcao'] = df['Números'].apply(eleva_ao_cubo)
df['cubo_lambda'] = df['Números'].apply(lambda x: x ** 3)

print(df)