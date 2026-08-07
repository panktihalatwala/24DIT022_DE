import os
import shutil
import pandas as pd
from datetime import datetime

# Folder paths
source_folder = "simulated_data"
quarantine_folder = "quarantine"

# Create quarantine folder if it doesn't exist
os.makedirs(quarantine_folder, exist_ok=True)

print("=" * 50)
print("SUPPLEMENTARY PROBLEM")
print("=" * 50)

# Check all CSV files inside simulated_data
for file in os.listdir(source_folder):

    if file.endswith(".csv"):

        filepath = os.path.join(source_folder, file)

        df = pd.read_csv(filepath)

        if "CustomerID" not in df.columns:

            shutil.move(filepath, os.path.join(quarantine_folder, file))

            with open("execution_log.txt", "a") as log:
                log.write("\n")
                log.write("=" * 40 + "\n")
                log.write(f"{datetime.now()}\n")
                log.write(f"{file} moved to quarantine.\n")
                log.write("Reason: Missing CustomerID\n")

            print(file, "moved to quarantine.")

        else:

            print(file, "passed validation.")

print("\nSupplementary validation completed.")