import pandas as pd

df = pd.read_csv("adc_data.csv")

df.columns = df.columns.str.strip()

print(df[["Time (seconds)", "ADC Value"]])
