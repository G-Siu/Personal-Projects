import pandas as pd

data = {
    "A": [5, 6, 8, 9, 7],
    "B": ["Flamingo", "Zebra", "Cart", "Bucket", "Samantha"],
    "C": ["Some", "Alex", "Apple", 5, "Art"]
}

df = pd.DataFrame(data)


# max_value = df[(df["B"].str.len() > 4) & (df["C"].str.startswith("A"))]["A"].max()
max_value = df[df["B"].str.len() > 4 & df["C"].str.startswith("A")]["A"].max()
print(max_value)