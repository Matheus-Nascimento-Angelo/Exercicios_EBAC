import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

df = pd.read_csv('C:\\Users\\mathe\\Documents\\estudos\\data-science\\Cientista_de_dados-EBAC\\materiais\\dados\\clientes-v2.csv')
df = df[['idade', 'salario']]

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Normalizando os dados;
norm_scaler = MinMaxScaler()
df['IdadeMinMaxScaler'] = norm_scaler.fit_transform(df[['idade']])
df['SalárioMinMaxScaler'] = norm_scaler.fit_transform(df[['salario']])
'''^^^^
 É preciso passar o df[['idade']] com dois colchetes porque o método fit_transform espera receber uma matriz 2d como argumento
 e se passarmos com apenas um colchete o método reconheceria como uma serie, ou seja, uma estrutura unidimensional, oque causaria
 um erro.
'''
# Normalizando os dados redefinindo os os valores de máximo e mínimo;
min_max_scaler = MinMaxScaler(feature_range=(-1, 1)) # Define o mínimo para -1 e o máximo para 1
df['IdadeStandardScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['SalarioStandardScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronizando os dados;
stand_scaler = StandardScaler()
df['IdadeStandardScaler'] = stand_scaler.fit_transform(df[['idade']])
df['SalárioStandardScaler'] = stand_scaler.fit_transform(df[['salario']])

# Padronização Robust Scaler;
robust_scaler = RobustScaler()
df['IdadeRobustScaler'] = robust_scaler.fit_transform(df[['idade']])
df['SalarioRobustScaler'] = robust_scaler.fit_transform(df[['salario']])

print('Normalização - de 0 a 1:')
print(f'Idade - Min: {df['IdadeMinMaxScaler'].min():.4f} Max: {df['IdadeMinMaxScaler'].max():.4f} Mean: {df['IdadeMinMaxScaler'].mean():.4f} Std: {df['IdadeMinMaxScaler'].std():.4f}')
print(f'Salário - Min: {df['SalárioMinMaxScaler'].min():.4f} Max: {df['SalárioMinMaxScaler'].max():.4f} Mean: {df['SalárioMinMaxScaler'].mean():.4f} Std: {df['SalárioMinMaxScaler'].std():.4f}\n')

print('Normalização - de -1 a 1:')
print(f'Idade - Min: {df['IdadeStandardScaler_mm'].min():.4f} Max: {df['IdadeStandardScaler_mm'].max():.4f} Mean: {df['IdadeStandardScaler_mm'].mean():.4f} Std: {df['IdadeStandardScaler_mm'].std():.4f}')
print(f'Salário - Min: {df['SalarioStandardScaler_mm'].min():.4f} Max: {df['SalarioStandardScaler_mm'].max():.4f} Mean: {df['SalarioStandardScaler_mm'].mean():.4f} Std: {df['SalarioStandardScaler_mm'].std():.4f}\n')

print('Padronização - ajusta a média para 0 e o desvio padrão para 1:')
print(f'Idade - Min: {df['IdadeStandardScaler'].min():.4f} Max: {df['IdadeStandardScaler'].max():.4f} Mean: {df['IdadeStandardScaler'].mean():.4f} Std: {df['IdadeStandardScaler'].std():.4f}')
print(f'Salário - Min: {df['SalárioStandardScaler'].min():.4f} Max: {df['SalárioStandardScaler'].max():.4f} Mean: {df['SalárioStandardScaler'].mean():.4f} Std: {df['SalárioStandardScaler'].std():.4f}\n')

print('RobustScaler (Ajuste a mediana e IQR):')
print(f'Idade - Min: {df['IdadeRobustScaler'].min():.4f} Max: {df['IdadeRobustScaler'].max():.4f} Mean: {df['IdadeRobustScaler'].mean():.4f} Std: {df['IdadeRobustScaler'].std():.4f}')
print(f'Salario - Min: {df['SalarioRobustScaler'].min():.4f} Max: {df['SalarioRobustScaler'].max():.4f} Mean: {df['SalarioRobustScaler'].mean():.4f} Std: {df['SalarioRobustScaler'].std():.4f}')