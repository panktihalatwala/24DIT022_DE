import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("simulated_data/customer_profiles.csv")

# Create SQLite database
conn = sqlite3.connect("customer.db")

# Store data in a table named 'customers'
df.to_sql("customers", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("Table Name: customers")
print("Total Records:", len(df))

conn.close()