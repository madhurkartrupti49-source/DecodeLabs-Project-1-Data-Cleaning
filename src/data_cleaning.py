import pandas as pd
import os

# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_FILE = os.path.join(BASE_DIR, "data", "raw_dataset.csv")
CLEANED_FILE = os.path.join(BASE_DIR, "data", "cleaned_dataset.csv")


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv(RAW_FILE)

print("========== BEFORE CLEANING ==========")

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ============================================================
# 2. HANDLE MISSING VALUES
# ============================================================

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")


# ============================================================
# 3. CONVERT DATE
# ============================================================

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


# ============================================================
# 4. REMOVE DUPLICATES
# ============================================================

df = df.drop_duplicates()


# ============================================================
# 5. VALIDATION
# ============================================================

print("\n========== AFTER CLEANING ==========")

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nInvalid Dates:")
print(df["Date"].isna().sum())


# ============================================================
# 6. DATA VALIDATION
# ============================================================

print("\n========== DATA VALIDATION ==========")

print("\nDuplicate Order IDs:")
print(df["OrderID"].duplicated().sum())

print("\nInvalid Dates:")
print(df["Date"].isna().sum())

print("\nInvalid Quantity:")
print((df["Quantity"] <= 0).sum())

print("\nInvalid UnitPrice:")
print((df["UnitPrice"] <= 0).sum())

print("\nInvalid ItemsInCart:")
print((df["ItemsInCart"] <= 0).sum())


calculated_total = df["Quantity"] * df["UnitPrice"]

incorrect_total = (
    (df["TotalPrice"] - calculated_total).abs() > 0.01
).sum()

print("\nIncorrect TotalPrice:")
print(incorrect_total)


# ============================================================
# 7. TEXT CLEANING
# ============================================================

text_columns = [
    "OrderID",
    "CustomerID",
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "TrackingNumber",
    "CouponCode",
    "ReferralSource"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


# ============================================================
# 8. SAVE CLEANED DATASET
# ============================================================

df.to_csv(CLEANED_FILE, index=False)


# ============================================================
# 9. FINAL STATUS
# ============================================================

print("\n========== FINAL STATUS ==========")
print("Data validation completed successfully.")
print("Cleaned dataset saved successfully!")
print("Location:", CLEANED_FILE)