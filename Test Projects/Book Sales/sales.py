# First, let's load the uploaded CSV file to understand its structure and the data it contains.
import pandas as pd

# Load the CSV file
sales_data = pd.read_csv('Book_Sales.csv')

# Display the first few rows of the dataframe to understand its structure
# print(sales_data.head())

# Cleaning the " Total Sales" column to remove the '€' symbol, commas, and leading whitespace, then converting it to float
sales_data['Total Sales Cleaned'] = sales_data[' Total Sales'].str.replace('€', '').str.replace(',', '').str.strip().astype(float)

# Grouping the data by 'Sales Channel' and 'Priority', then calculating the average total sales amount for each group
average_sales = sales_data.groupby(['Sales Channel', 'Priority'])['Total Sales Cleaned'].mean().reset_index()

# Identifying the combination of sales channel and priority level with the highest average total sales amount
highest_average_sales = average_sales.loc[average_sales['Total Sales Cleaned'].idxmax()]

print(average_sales, highest_average_sales)
