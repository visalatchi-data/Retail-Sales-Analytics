import pandas as pd

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", None)
pd.options.display.float_format = "{:,.2f}".format

# Same path as in 01_load_data.py
df = pd.read_csv(r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv")

print("Shape:", df.shape)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- Duplicate Order_IDs ---")
print(df["Order_ID"].duplicated().sum())

print("\n--- Summary Stats ---")
print(df.describe())
