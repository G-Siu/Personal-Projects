import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("sushi_earns.csv")

# Fill missing `Cash_price` with 0
df['Cash_price'] = df['Cash_price'].fillna(0)

# Calculate profit margin for each payment type
df['profit_margin_cash'] =  (df['Cash_price'] - df['total_cost']) / df['Cash_price']
df['profit_margin_pedidosya'] = (df['pedidosya_price'] - df['total_cost']) / df['pedidosya_price']
df['profit_margin_shea_app'] = (df['Shea_app_price'] - df['total_cost']) / df['Shea_app_price']

# Calculate average profit margin
df['profitability_score'] = (
    df['profit_margin_cash']
    + df['profit_margin_pedidosya']
    + df['profit_margin_shea_app']
) / 3

# Group by `Menu_product` and sort by `profitability_score`
df_grouped = df.groupby('Menu_product').agg({'profitability_score': 'mean', 'total_cost': 'sum'}).sort_values(by='profitability_score', ascending=False)

# Filter the dataframe to include products with non-zero cost
df_non_zero_cost = df_grouped[df_grouped['total_cost'] != 0].copy()

# Get the ranking
df_non_zero_cost['profitability_ranking'] = (
    df_non_zero_cost['profitability_score'].rank(ascending=False)
)

df['desc_length'] = df['Desc'].apply(lambda x: len(str(x).split()))

# Join the description length with the rankings
df_analysis = df_non_zero_cost.merge(
    df[['Menu_product', 'desc_length']], on='Menu_product', how='left'
)

# Compute the correlation between profitability score and description length
correlation = df_analysis['profitability_score'].corr(df_analysis['desc_length'])

print(f'The correlation between profitability and description length is: {correlation:.3f}')
