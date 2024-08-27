import pandas as pd

# Read all sheet names from the Excel file
xls = pd.ExcelFile('Invoices_to_be_paid.xlsx')
all_sheet_names = xls.sheet_names

# Filter out empty sheet names and duplicates
non_empty_sheet_names = [sheet for sheet in all_sheet_names if sheet.strip() != '']
unique_sheet_names = list(set(non_empty_sheet_names))

if (len(unique_sheet_names) > 10):
  # Sample 10 sheet names if there are too many
  print(f"The file has {len(unique_sheet_names)} sheets. Here's a sample of 10:")
  print(pd.Series(unique_sheet_names).sample(10).tolist())
else:
  # Otherwise print all unique sheet names
  print(f"The file has {len(unique_sheet_names)} sheets. All sheet names are:")
  print(unique_sheet_names)