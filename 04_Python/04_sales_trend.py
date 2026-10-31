import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
pd.options.display.float_format = "{:,.2f}".format

path = r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv"
df = pd.read_csv(path)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

#Month-wise Sales & Profit
df["Year_Month"] = df["Order_Date"].dt.to_period("M")
monthly = df.groupby("Year_Month")[["Sales", "Profit"]].sum()
print(monthly)

#Line chart
plt.figure(figsize=(10,5))
plt.plot(monthly.index.astype(str), monthly["Sales"], marker="o", label="Sales")
plt.plot(monthly.index.astype(str), monthly["Profit"], marker="o", label="Profit")
plt.title("Monthly Sales & Profit Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.savefig(r"D:\Data_Analyst_Portfolio\04_Python\monthly_trend.png", dpi=150)
plt.show()
