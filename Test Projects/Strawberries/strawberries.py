import pandas as pd

strawberry_data = pd.read_csv("STRAWBERRY SALES 2023 - Sheet1.tsv", sep="\t")

print(strawberry_data.head().to_markdown(index=False, numalign="left", stralign="left"))

print(strawberry_data.info())

organic = strawberry_data[strawberry_data["Unnamed: 7"].str.strip().str.upper(
) == "ORGANIC"]

print(organic)
