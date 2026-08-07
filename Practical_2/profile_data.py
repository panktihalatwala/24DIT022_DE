import pandas as pd
import json

print("=" * 50)
print("DATA PROFILING REPORT")
print("=" * 50)

# -----------------------------
# Profile Customer CSV
# -----------------------------
print("\nCustomer Profiles (CSV)")
print("-" * 30)

df = pd.read_csv("simulated_data/customer_profiles.csv")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# -----------------------------
# Profile JSON
# -----------------------------
print("\n\nAPI Transactions (JSON)")
print("-" * 30)

with open("simulated_data/api_transactions.json", "r") as file:
    transactions = json.load(file)

print("Total Transactions:", len(transactions))

print("\nKeys in JSON:")
print(transactions[0].keys())

print("\nNested Payment Object:")
print(transactions[0]["payment"])

# -----------------------------
# Profile Config File
# -----------------------------
print("\n\nConfiguration File")
print("-" * 30)

with open("simulated_data/config.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))

empty_lines = sum(1 for line in lines if line.strip() == "")
print("Empty Lines:", empty_lines)

print("\nContents:")
for line in lines:
    print(line.strip())