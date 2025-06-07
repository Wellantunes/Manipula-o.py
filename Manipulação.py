import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Carrega o DataFrame
df = pd.read_csv('ecommerce_tratados.csv')

# Verifique o nome exato das colunas (opcional, mas útil)
print(df.columns)

# Instancia o MinMaxScaler
scaler = MinMaxScaler()

# Normalizações com MinMaxScaler
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliações']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preço']])

# Instancia o LabelEncoder
le = LabelEncoder()

# Codificações com LabelEncoder
df['Marca_Cod'] = le.fit_transform(df['Marca'])
df['Material_Cod'] = le.fit_transform(df['Material'])
df['Temporada_Cod'] = le.fit_transform(df['Temporada'])

# Visualiza os primeiros registros (opcional)
print(df.head())