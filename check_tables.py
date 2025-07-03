import pandas as pd

# Load the Excel file
xls = pd.ExcelFile("data/capbudg.xls")

# Print all sheet names (these are your "table names")
print("Sheet Names (Table Names):")
print(xls.sheet_names)
