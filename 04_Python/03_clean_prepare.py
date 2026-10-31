import pandas as pd

pd.set_option("display.max_columns",None)
pd.set_option("display.width",250)
pd.options.display.float_format = "{:,.2f}".format

path = r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv"
df = pd.read_csv(path)

#Order_Date as date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print(df.dtypes["Order_Date"])

#Loss-making orders count
loss = df[df["Profit"] < 0]
print("\nLoss orders:", len(loss))
print("Total loss amount:", round(loss["Profit"].sum(),2))

#Category-wise Sales & Profit
print("\n--- Category Summary ---")
print(df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False))
