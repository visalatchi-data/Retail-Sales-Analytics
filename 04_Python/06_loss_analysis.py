import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 250)
pd.options.display.float_format = "{:,.2f}".format

path = r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv"
df = pd.read_csv(path)

loss = df[df["Profit"] < 0]

print("Total orders:", len(df))
print("Loss orders:", len(loss))
print("Loss %:", round(len(loss) / len(df) * 100, 2))
print("Total loss:", round(loss["Profit"].sum(), 2))

# Category-wise loss
print("\n--- Loss by Category ---")
print(loss.groupby("Category")["Profit"].agg(["count", "sum"]).sort_values("sum"))

# Region-wise loss
print("\n--- Loss by Region ---")
print(loss.groupby("Region")["Profit"].agg(["count", "sum"]).sort_values("sum"))

# Product-wise loss
print("\n--- Loss by Product ---")
print(loss.groupby("Product")["Profit"].agg(["count", "sum"]).sort_values("sum"))

# Discount vs Profit (all orders)
print("\n--- Discount vs Avg Profit ---")
disc = df.groupby("Discount").agg(Orders=("Profit", "count"),
                                  Avg_Profit=("Profit", "mean"),
                                  Loss_Orders=("Profit", lambda x: (x < 0).sum()))
print(disc)

# Charts
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

loss.groupby("Category")["Profit"].sum().sort_values().plot(kind="bar", ax=axes[0], color="firebrick")
axes[0].set_title("Total Loss by Category")
axes[0].set_ylabel("Loss Amount")
axes[0].tick_params(axis="x", rotation=0)

disc["Loss_Orders"].plot(kind="bar", ax=axes[1], color="darkorange")
axes[1].set_title("Loss Orders by Discount Level")
axes[1].set_xlabel("Discount")
axes[1].set_ylabel("No. of Loss Orders")
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig(r"D:\Data_Analyst_Portfolio\04_Python\loss_analysis.png", dpi=150)
plt.show()
