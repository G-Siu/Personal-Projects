import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "sales_memos.csv"
sales_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
sales_data.head()

# Count the occurrences of each customer
customer_counts = sales_data['Customer'].value_counts()

# Plot the data
plt.figure(figsize=(10, 8))
customer_counts.plot(kind='bar')
plt.title('Customer Recurrence')
plt.xlabel('Customer')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Show the plot
plt.show()
