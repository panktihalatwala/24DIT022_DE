import pandas as pd
import re
from datetime import datetime

# Read CSV file
df = pd.read_csv("simulated_data/customer_profiles.csv")

print("=" * 50)
print("DATA QUALITY CHECK")
print("=" * 50)

# -----------------------------
# Check Missing Values
# -----------------------------
missing = df.isnull().sum()
print("\nMissing Values:")
print(missing)

# -----------------------------
# Check Duplicate Customer IDs
# -----------------------------
duplicate_ids = df["CustomerID"].duplicated().sum()
print("\nDuplicate Customer IDs:", duplicate_ids)

# -----------------------------
# Check Invalid Emails
# -----------------------------
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

invalid_email = df[
    ~df["Email"].astype(str).str.match(email_pattern, na=False)
]

print("Invalid Emails:", len(invalid_email))

# -----------------------------
# Check Invalid Age
# -----------------------------
invalid_age = df[(df["Age"] < 18) | (df["Age"] > 60)]

print("Invalid Age Records:", len(invalid_age))

# -----------------------------
# Overall Status
# -----------------------------
if (
    missing.sum() == 0
    and duplicate_ids == 0
    and len(invalid_email) == 0
    and len(invalid_age) == 0
):
    status = "PASS"
else:
    status = "FAIL"

print("\nOverall Status:", status)

# -----------------------------
# Save Execution Log
# -----------------------------
with open("execution_log.txt", "w") as log:
    log.write("DATA QUALITY EXECUTION LOG\n")
    log.write("==========================\n")
    log.write(f"Date: {datetime.now()}\n\n")
    log.write(f"Missing Values:\n{missing}\n\n")
    log.write(f"Duplicate Customer IDs: {duplicate_ids}\n")
    log.write(f"Invalid Emails: {len(invalid_email)}\n")
    log.write(f"Invalid Age Records: {len(invalid_age)}\n")
    log.write(f"\nOverall Status: {status}\n")

print("\nExecution log saved successfully.")