import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Connect to SQLite
conn = sqlite3.connect("sales_data.db")
query = """
SELECT
    product, SUM(quantity) AS total_qty,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

print(df)

df.plot(kind='bar', x='product', y='revenue')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
