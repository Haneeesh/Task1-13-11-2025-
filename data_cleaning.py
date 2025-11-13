# ===============================
# Data Cleaning Task
# ===============================

import pandas as pd

# 1️⃣ Load the dataset
df = pd.read_csv("KaggleV2-May-2016.csv")

# 2️⃣ Identify missing values
print("Missing values per column:\n", df.isnull().sum())

# (Optional) Handle missing values if any (fill or drop)
df = df.dropna()  # or df.fillna(value)

# 3️⃣ Remove duplicate rows
df = df.drop_duplicates()
print(f"After removing duplicates: {df.shape}")

# 4️⃣ Standardize text values (example: Gender column)
# Convert all text to lowercase and remove spaces
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.lower()
    # Optional: Replace inconsistent labels
    df['Gender'] = df['Gender'].replace({'f': 'female', 'm': 'male'})

# 5️⃣ Convert date formats to a consistent type
date_columns = ['ScheduledDay', 'AppointmentDay']
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime("%d-%m-%Y")

# 6️⃣ Rename column headers to be clean and uniform
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 7️⃣ Check and fix data types
# Example: Ensure age is integer and date columns are datetime
if 'age' in df.columns:
    df['age'] = df['age'].astype(int)

for col in ['scheduledday', 'appointmentday']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format="%d-%m-%Y", errors='coerce')

# 8️⃣ Save the cleaned dataset
df.to_csv("Cleaned_KaggleV2.csv", index=False)
print("✅ Data cleaning complete. Cleaned file saved as 'Cleaned_KaggleV2.csv'.")
