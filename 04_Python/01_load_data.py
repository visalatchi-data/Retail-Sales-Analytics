import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",200)
pd.options.display.float_format = "{:,.2f}".format

path = r"D:\Data_Analyst_Portfolio\02_Excel_Cleaning\Retail_Sales_Cleaned.csv"
df = pd.read_csv(path)

print("Shape:", df.shape)
print(df.head())
