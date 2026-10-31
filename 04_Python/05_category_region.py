import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
pd.options.display.float_format = "{:,.2f}".format

path = r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv"
df = pd.read_csv(path)

# Category-wise
category = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
print(category)

# Region-wise
region = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
print(region)

# Two charts side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

category.plot(kind="bar", ax=axes[0])
axes[0].set_title("Category-wise Sales & Profit")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Amount")
axes[0].tick_params(axis="x", rotation=0)
axes[0].ticklabel_format(style="plain", axis="y")

region.plot(kind="bar", ax=axes[1])
axes[1].set_title("Region-wise Sales & Profit")
axes[1].set_xlabel("Region")
axes[1].set_ylabel("Amount")
axes[1].tick_params(axis="x", rotation=0)
axes[1].ticklabel_format(style="plain", axis="y")

plt.tight_layout()
plt.savefig(r"D:\Data_Analyst_Portfolio\04_Python\category_region.png", dpi=150)
plt.show()
