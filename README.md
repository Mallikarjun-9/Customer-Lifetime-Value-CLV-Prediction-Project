# Customer Lifetime Value (CLV) Prediction Project

## 📌 Project Overview
This project aims to predict Customer Lifetime Value (CLV) using historical transactional data from an e-commerce dataset. It was developed during a Data Analyst Internship at **Elevate Labs** as part of the final submission requirement.

---

## 📄 Abstract
Customer Lifetime Value (CLV) is a key business metric that estimates the total worth of a customer throughout their relationship with the company. By predicting CLV, businesses can make more informed decisions on customer retention, marketing spend, and profitability. This project uses Python and machine learning techniques to predict CLV based on transaction behavior.

---

## 🛠 Tools & Technologies Used
- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- **Jupyter Notebook / IDLE**
- **Machine Learning**: Random Forest Regressor
- **Data Visualization**: Seaborn, Matplotlib

---

## 📊 Dataset Description
The dataset used is the **Online Retail Dataset**. Key columns include:
- `InvoiceNo`, `StockCode`, `Description`, `Quantity`
- `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`

---

## 🔄 Data Preprocessing
- Removed missing Customer IDs
- Converted `InvoiceDate` to datetime format
- Calculated:
  - **Recency**: Days since last purchase
  - **Frequency**: Total number of purchases
  - **Monetary (AOV)**: Average order value
- Created `TotalPrice = Quantity * UnitPrice`

---

## 📈 Model Building
- Features used: `Recency`, `Frequency`, `AOV`
- Target: `Customer Lifetime Value (CLV)`
- Model: **Random Forest Regressor**
- Output: CLV predictions segmented as:
  - High Value (CLV > 5000)
  - Medium Value (2000 < CLV ≤ 5000)
  - Low Value (CLV ≤ 2000)
    
---

## ✅ Desired Output Format (Sample)

| CustomerID | Recency | Frequency | AOV   | Predicted CLV | Segment     |
|------------|---------|-----------|-------|---------------|-------------|
| 12345      | 42      | 7         | 43.50 | 3154.78       | Medium      |
| 23456      | 5       | 12        | 88.20 | 7480.33       | High        |
| 34567      | 200     | 2         | 12.00 | 540.22        | Low         |

---

## 📊 Visualizations

Below are some visualizations created during the EDA and prediction steps:

### CLV Distribution by Segment
![CLV Segment Distribution](https://github.com/Mallikarjun-9/Customer-Lifetime-Value-CLV-Prediction-Project/blob/02ba8e4eb18cbb8a0770b17e44507ae0144c75b0/Figure_1.png)

---

## 📌 Project Steps
1. **Data Cleaning & Feature Engineering**
2. **Exploratory Data Analysis (EDA)**
3. **CLV Calculation & Labeling**
4. **Model Training & Prediction**
5. **Segmentation and Interpretation**

---

## ✅ Conclusion
The project successfully predicted CLV using transaction patterns and helped segment customers into meaningful groups. This approach can help businesses allocate resources efficiently and focus on high-value customers for better ROI.

---

## 🧑‍💻 Author
- **Role**: Data Analyst Intern  
- **Organization**: Elevate Labs  
- **Duration**: April 2025 – May 2025 (Remote)

