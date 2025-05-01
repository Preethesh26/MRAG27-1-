import pandas as pd
import json

# Load Excel file
df = pd.read_excel(r"D:\1\1\unique_grouped_output1.xlsx")  # Make sure this file is in the same folder

# Fill blank/merged cells in 'Health Issue' column
df['Health Issue'] = df['Health Issue'].fillna(method='ffill')

# Group by 'Health Issue'
grouped = df.groupby('Health Issue').apply(
    lambda x: x.drop(columns='Health Issue').to_dict(orient='records')
).to_dict()

# Save to JSON
with open("grouped_medicines.json", "w", encoding='utf-8') as f:
    json.dump(grouped, f, indent=2, ensure_ascii=False)

print("✅ Grouped JSON saved as grouped_medicines.json")
