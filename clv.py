import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv(r"C:\Users\Asus\Downloads\online+retail\Online Retail.csv", encoding="ISO-8859-1")
# Drop missing CustomerIDs
df.dropna(subset=["CustomerID"], inplace=True)

# Remove negative or zero quantities and prices
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], dayfirst=True)


# Calculate TotalPrice
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Reference date for Recency
latest_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Create RFM table
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (latest_date - x.max()).days,
    "InvoiceNo": "nunique",
    "TotalPrice": "sum"
}).reset_index()

rfm.columns = ["CustomerID", "Recency", "Frequency", "Monetary"]

# Calculate AOV (Average Order Value)
rfm["AOV"] = rfm["Monetary"] / rfm["Frequency"]

# Target variable: LTV (assume total monetary value = LTV)
rfm["LTV"] = rfm["Monetary"]

# Features and target
features = rfm[["Recency", "Frequency", "AOV"]]
target = rfm["LTV"]

# Train-test split (random split)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# Feature Importance
importances = model.feature_importances_
plt.figure(figsize=(6, 4))
plt.barh(features.columns, importances)
plt.title("Feature Importances")
plt.show()

# Predict LTV for all customers
rfm["PredictedLTV"] = model.predict(features)

# Segment based on predicted LTV
def segment(ltv):
    if ltv > rfm["PredictedLTV"].quantile(0.66):
        return "High"
    elif ltv > rfm["PredictedLTV"].quantile(0.33):
        return "Medium"
    else:
        return "Low"

rfm["Segment"] = rfm["PredictedLTV"].apply(segment)

# Final columns to export
output = rfm[["CustomerID", "Recency", "Frequency", "AOV", "PredictedLTV", "Segment"]]

# Create directory if it doesn't exist
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)


# Save to CSV
output.to_csv(os.path.join(output_dir, r"C:\Users\Asus\Downloads\online+retail\ltv_predictions.csv"), index=False)
print("✅ LTV predictions saved successfully!")
