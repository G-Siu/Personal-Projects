import pandas as pd
import numpy as np

df = pd.read_csv("Account Balance Base - Hoja1.tsv", sep='\t')

print(df.head())
print(df.info())

balance = df[" Balance"].str.replace("$ ", "").replace("-", "NaN")
print(balance)

median = np.median(df[" Balance"])

print(median)
