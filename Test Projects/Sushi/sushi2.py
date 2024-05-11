import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("sushi_earns.csv")

# Assuming the previous steps for calculating profitability scores are correct and still applicable
# Fill missing `Cash_price` with 0
df['Cash_price'] = df['Cash_price'].fillna(0)

# Calculate profit margin for each payment type
df['profit_margin_cash'] =  (df['Cash_price'] - df['total_cost']) / df['Cash_price']
df['profit_margin_pedidosya'] = (df['pedidosya_price'] - df['total_cost']) / df['pedidosya_price']
df['profit_margin_shea_app'] = (df['Shea_app_price'] - df['total_cost']) / df['Shea_app_price']

# Calculate average profit margin (profitability score)
df['profitability_score'] = (
    df['profit_margin_cash'] + df['profit_margin_pedidosya'] + df['profit_margin_shea_app']
) / 3

# Calculate the length of the description for each product
df['desc_length'] = df['Desc'].apply(lambda x: len(str(x)))

# Filter out products with non-zero cost
df_non_zero_cost = df[df['total_cost'] > 0]

# Rank the products based on profitability score
df_non_zero_cost_ranked = df_non_zero_cost.sort_values(by='profitability_score', ascending=False)

# Select relevant columns for correlation analysis
df_correlation = df_non_zero_cost_ranked[['profitability_score', 'desc_length']]

# Calculate the correlation
correlation = df_correlation.corr()

print(correlation)