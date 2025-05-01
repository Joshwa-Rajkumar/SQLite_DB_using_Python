import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Create database and table
conn = sqlite3.connect("college_data.db")
cursor = conn.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS college (
    student_id INT PRIMARY KEY,
    student_name TEXT,
    department TEXT,
    doj DATE,
    fee INT)
""")


# Clear existing data
cursor.execute("DELETE from college")

# Inser sample data
data = [
    (103021, 'Joshwa Rajkumar', 'Civil', '2018-06-01', 40000),
    (104022, 'Vignesh', 'Mechanical', '2018-06-01', 45000),
    (103145, 'Marimuthu','Civil', '2020-07-01', 15000),
    (105122, 'Muthu', 'ECE', '2019-01-20', 20000)
    ]

cursor.executemany("INSERT INTO college (student_id, student_name, department, doj, fee) VALUES (?,?,?,?,?)", data)
conn.commit()

query = """
    SELECT department, SUM(fee)
    FROM college
    GROUP BY department
    ORDER BY fee """

cursor.execute(query)
result = cursor.fetchall()

print("department\t fee\n")
for row in result:
    print("{:<10}, {:<10}".format (row[0], row[1]))


#Visualizing data
df = pd.read_sql_query(query, conn)
departments = [row[0] for row in result]
fees = [row[1] for row in result]

plt.figure(figsize=(10,6))
plt.pie(fees, labels=departments, autopct='%1.1f%%', startangle=140)
plt.title("Total Fees collected by Department")
plt.axis('equal')
plt.tight_layout()
plt.savefig("College_sales.png")
plt.show()
