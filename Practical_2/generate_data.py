from faker import Faker
import pandas as pd
import json
import random
import os

# Initialize Faker
fake = Faker()

# Create simulated_data folder if it doesn't exist
os.makedirs("simulated_data", exist_ok=True)

# -----------------------------
# Generate Customer Profiles CSV
# -----------------------------
customers = []

for i in range(1, 101):
    customers.append({
        "CustomerID": i,
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "City": fake.city(),
        "Age": random.randint(18, 60)
    })

df = pd.DataFrame(customers)
df.to_csv("simulated_data/customer_profiles.csv", index=False)

# -----------------------------
# Generate API Transactions JSON
# -----------------------------
transactions = []

for i in range(1, 101):
    transactions.append({
        "transaction_id": i,
        "customer_id": random.randint(1, 100),
        "payment": {
            "method": random.choice(["UPI", "Card", "Cash"]),
            "amount": random.randint(100, 5000)
        },
        "status": random.choice(["Success", "Failed", "Pending"])
    })

with open("simulated_data/api_transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)

# -----------------------------
# Generate Config File
# -----------------------------
with open("simulated_data/config.txt", "w") as file:
    file.write("Server=localhost\n")
    file.write("Port=5432\n")
    file.write("Database=customerdb\n")
    file.write("Username=admin\n")
    file.write("Password=admin123\n")

print("Data generated successfully!")
print("Files saved in simulated_data folder.")