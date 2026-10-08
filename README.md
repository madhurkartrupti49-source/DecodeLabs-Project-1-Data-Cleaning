# DecodeLabs Project 1 – Data Cleaning & Preparation

## 📌 Project Overview

This project focuses on cleaning and preparing a raw e-commerce transaction dataset for further data analysis.

The main objective is to improve data quality by identifying and handling missing values, duplicate records, incorrect data formats, and invalid numerical values.

This project was completed as part of the DecodeLabs Industrial Training Kit – Data Analytics.

---

## 🎯 Objectives

- Identify missing values in the dataset.
- Handle missing data appropriately.
- Detect and remove duplicate records.
- Convert dates into the correct format.
- Validate numerical columns.
- Verify calculated values such as TotalPrice.
- Clean unwanted spaces from text fields.
- Generate a final cleaned dataset ready for analysis.

---

## 📂 Dataset Information

The dataset contains **1,200 records and 14 columns** related to customer orders.

### Main Columns

| Column | Description |
|---|---|
| OrderID | Unique order identifier |
| Date | Order date |
| CustomerID | Customer identifier |
| Product | Product purchased |
| Quantity | Quantity ordered |
| UnitPrice | Price per unit |
| ShippingAddress | Customer shipping address |
| PaymentMethod | Payment method used |
| OrderStatus | Current order status |
| TrackingNumber | Shipment tracking number |
| ItemsInCart | Number of items in cart |
| CouponCode | Coupon applied to the order |
| ReferralSource | Source through which customer arrived |
| TotalPrice | Total order price |

---

## 🛠️ Data Cleaning Process

### 1. Dataset Inspection

The raw dataset was inspected to identify:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate records

Initial dataset:

- Rows: **1,200**
- Columns: **14**

---

### 2. Missing Value Handling

The `CouponCode` column contained **309 missing values**.

Since a missing coupon indicates that no coupon was applied, the missing values were replaced with:

```text
No Coupon