# Sales Data Management & Visualization Using SQLite and Python

This project involves managing and analyzing product sales data using SQLite and Python. It includes creating a database, inserting product sales records, querying total sales by product, and visualizing the results using pie charts.

---

## 🗃️ Step 1: Database and Table Creation

- A new SQLite database file named `sales_data.db` is created.
- A table named `sales` is created with the following fields:
  - `product` (Name of the product sold)
  - `quantity` (Number of units sold)
  - `price` (Price per unit)

- The table is created conditionally using `IF NOT EXISTS` to avoid duplication.

---

## 📥 Step 2: Inserting Sales Data

- A list of product sales records is inserted using `executemany` for efficient bulk entry.
- Example products include:
  - Keyboard
  - Mouse
  - Monitor
  - Printer

- Each entry includes the product name, quantity sold, and price.

---

## 📊 Step 3: Querying Sales Summary

- A SQL query calculates total revenue for each product using:
  - `quantity * price` for each record
  - Aggregation using `GROUP BY product`
  - Sorting in descending order by total revenue

---

## 🖥️ Step 4: Console Output

- The query results are printed in the terminal using aligned formatting for readability.
- Headers and values are aligned using string formatting techniques.

---

## 📈 Step 5: Data Visualization – Pie Chart

- A pie chart is generated to represent each product’s share of total sales revenue.
- Labels display the product name and percentage.
- `matplotlib.pyplot` is used with `axis("equal")` for a circular chart.

---

## ✅ Final Output

- Console displays total revenue per product in a readable table format.
- A pie chart visually illustrates each product’s contribution to total revenue.

---

## 🔍 Key Concepts Covered

- SQLite database creation and usage in Python
- Safe and bulk insertion of records
- SQL aggregation and sorting for reporting
- Console output formatting using f-strings
- Visual representation of grouped data using pie charts

---

## 🛠️ Tools & Technologies Used

- Python 3.11
- SQLite3 (Python standard library)
- Matplotlib for pie chart visualization
- IDLE (Python's built-in IDE)
