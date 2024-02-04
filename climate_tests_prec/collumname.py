import pandas as pd

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv('/home/gabriel/Downloads/archive(1)/GlobalLandTemperaturesByCity.csv')

# Obtenha os nomes das colunas
nomes_das_colunas = df.columns

# Exiba os nomes das colunas
print(nomes_das_colunas)
