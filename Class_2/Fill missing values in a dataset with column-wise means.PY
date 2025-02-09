import pandas as pd

df = pd.read_csv("Class_2\weather_report.csv")
print("The CSV file:")
print(df)

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):  
        df[col].fillna(df[col].mean(), inplace=True)   
print("Afer fill missing values:")
print(df)