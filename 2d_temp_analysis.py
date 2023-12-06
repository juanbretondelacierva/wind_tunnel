import pandas as pd
df = pd.read_excel(io="2D/0/1sigma_2023-12-01_09-22-11.csv", sheet_name="1sigma_2023-12-01_09-22-11")

a = df.as_matrix()

print(df.head(5))