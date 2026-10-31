import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
pd.options.display.float_format = "{:,.2f}".format

path = r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv"
df = pd.read_csv(path)

# Top Products
products = df.groupby("Product")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False).head(10)
print("--- Top 10 Products ---")
print(products)

# Top States
states = df.groupby("State")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False).head(10)
print("\n--- Top 10 States ---")
print(states)

# Charts
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

products["Sales"].sort_values().plot(kind="barh", ax=axes[0], color="steelblue")
axes[0].set_title("Top 10 Products by Sales")
axes[0].set_xlabel("Sales")
axes[0].ticklabel_format(style="plain", axis="x")

states["Sales"].sort_values().plot(kind="barh", ax=axes[1], color="seagreen")
axes[1].set_title("Top 10 States by Sales")
axes[1].set_xlabel("Sales")
axes[1].ticklabel_format(style="plain", axis="x")

plt.tight_layout()
plt.savefig(r"D:\Data_Analyst_Portfolio\04_Python\top_products_states.png", dpi=150)
plt.show()
