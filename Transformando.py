import pandas as pd

# Carrega o DataFrame
df = pd.read_csv('ecommerce_tratados.csv')

# 1. Mapeia 'Qtd_Vendidos' para valores numéricos
mapa_vendas = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(mapa_vendas)

# 2. Frequência relativa da 'Marca' (não afeta os testes, mas manteremos consistente)
df['Marca_Freq'] = df['Marca'].map(df['Marca'].value_counts() / len(df))

# 3. Frequência relativa da 'Material' com base em TODO o DataFrame (incluindo NaN)
df['Material_Freq'] = df['Material'].map(df['Material'].value_counts() / len(df))

# Visualização (opcional)
print(df[['Qtd_Vendidos', 'Qtd_Vendidos_Cod', 'Marca', 'Marca_Freq', 'Material', 'Material_Freq']].head())