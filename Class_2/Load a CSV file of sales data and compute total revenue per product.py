import pandas as pd

df = pd.read_csv("Class_2\software_selling_sheet.csv") 

df["Revenue"] = df["Quantity"] * df["Price"]


total_revenue = df.groupby("Product Name")["Revenue"].sum()

print("Total Revenue per product :",total_revenue)