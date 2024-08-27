import pandas as pd

transactions = pd.read_csv("transactions-2023-12-01-2024-01-01.csv")

# print(transactions.head())

transactions["Discounts"] = (
    transactions["Discounts"].str.replace("$", "").astype(float))
print(transactions["Discounts"])

transactions["Service Charges"] = (
    transactions[("Service Charges")].str.replace("$", "").astype(float))

print(transactions["Service Charges"])

count_discounts = 0
count_service_charges = 0

for index in range(0, 75):
    if transactions["Discounts"][index] < 0:
        count_discounts += 1
    if transactions["Service Charges"][index] < 0:
        count_service_charges += 1

print("Discount values less than 0:", count_discounts)
print("Service charges less than 0:", count_service_charges)