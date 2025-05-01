import sqlite3

# Create database and table
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
  id INT PRIMARY KEY,
  customer text,
  product text,
  quantity INT,
  unit_price real,
  total_price real,
  sale_date DATE
)
""")

# Clear existing data
cursor.execute("delete from sales")

# Insert sample data
data = [
    ('1', 'Drew Bennett', 'Keyboard', '5', '1068.14', '5340.7', '2024-10-03'),
('2', 'Sarah Scott', 'Smartphone', '2', '423.4', '846.8', '2024-06-10'),
('3', 'Barbara Atkinson', 'Monitor', '3', '1004.04', '3012.12', '2024-12-04'),
('4', 'Mark Walker', 'Mouse', '3', '856.0', '2568.0', '2024-08-29'),
('5', 'Gabriella Ali', 'Mouse', '5', '467.44', '2337.2', '2025-01-22'),
('6', 'Ashley Williams', 'Headphones', '2', '437.4', '874.8', '2024-07-12'),
('7', 'Eric Kane', 'Monitor', '1', '1497.8', '1497.8', '2024-07-08'),
('8', 'Robin White', 'Monitor', '1', '666.54', '666.54', '2024-10-11'),
('9', 'Dr. Allison Meyers', 'Monitor', '5', '77.05', '385.25', '2024-11-12'),
('10', 'Timothy Webb', 'Mouse', '1', '259.35', '259.35', '2024-12-02'),
('11', 'Larry Blair', 'Keyboard', '5', '1114.7', '5573.5', '2024-04-30'),
('12', 'Erica Clark', 'Mouse', '3', '1346.37', '4039.11', '2025-01-04'),
('13', 'Evan Black', 'Smartphone', '4', '76.59', '306.36', '2025-02-11'),
('14', 'Kristy Anderson', 'Laptop', '4', '107.3', '429.2', '2025-04-04'),
('15', 'Regina Cummings', 'Smartphone', '1', '486.11', '486.11', '2024-05-30'),
('16', 'Michaela Smith', 'Monitor', '1', '715.93', '715.93', '2024-11-29'),
('17', 'Spencer Brown', 'Keyboard', '4', '250.05', '1000.2', '2024-10-05'),
('18', 'Karen Henderson', 'Headphones', '2', '101.01', '202.02', '2025-02-08'),
('19', 'Christina George', 'Mouse', '5', '1367.02', '6835.1', '2024-11-05'),
('20', 'Lisa Eaton', 'Mouse', '3', '1319.95', '3959.85', '2025-02-14'),
('21', 'Jamie Gardner', 'Monitor', '4', '1073.06', '4292.24', '2024-07-18'),
('22', 'Joseph Booker', 'Laptop', '1', '545.49', '545.49', '2024-07-07'),
('23', 'Brittany Martin', 'Mouse', '1', '246.68', '246.68', '2025-02-19'),
('24', 'Tammy Lynch', 'Mouse', '3', '1312.25', '3936.75', '2024-08-04'),
('25', 'Lisa Wilson', 'Laptop', '4', '944.14', '3776.56', '2024-11-04'),
('26', 'Mary Walker', 'Monitor', '3', '1245.72', '3737.16', '2024-07-17'),
('27', 'Rick Stone', 'Keyboard', '5', '74.88', '374.4', '2025-03-25'),
('28', 'Megan Ponce', 'Monitor', '4', '1438.77', '5755.08', '2024-09-05'),
('29', 'Chad Simmons', 'Monitor', '3', '405.07', '1215.21', '2024-08-24'),
('30', 'Christina Gonzales', 'Mouse', '1', '1089.15', '1089.15', '2024-06-29'),
('31', 'Megan Morris', 'Laptop', '4', '1259.94', '5039.76', '2024-10-18'),
('32', 'Victor Ward', 'Smartphone', '3', '923.29', '2769.87', '2025-03-27'),
('33', 'Juan Simmons', 'Monitor', '5', '62.43', '312.15', '2024-08-26'),
('34', 'Sharon Potts', 'Laptop', '3', '437.42', '1312.26', '2025-04-22'),
('35', 'Matthew Hicks', 'Smartphone', '4', '141.63', '566.52', '2024-05-09'),
('36', 'Heather Carr', 'Laptop', '1', '751.79', '751.79', '2024-07-16'),
('37', 'Catherine Thomas', 'Monitor', '3', '662.9', '1988.7', '2024-05-01'),
('38', 'Andrea Woods', 'Keyboard', '4', '432.1', '1728.4', '2025-01-16'),
('39', 'Lisa Moss', 'Monitor', '4', '418.43', '1673.72', '2024-10-14'),
('40', 'Tyler Roberts', 'Keyboard', '5', '1157.4', '5787.0', '2024-05-24'),
('41', 'Carla Anderson', 'Laptop', '1', '1291.04', '1291.04', '2024-08-02'),
('42', 'Sharon Ferguson', 'Smartphone', '2', '131.51', '263.02', '2025-04-21'),
('43', 'Alexa Cox', 'Keyboard', '3', '1042.51', '3127.53', '2025-03-02'),
('44', 'Gary Brown', 'Keyboard', '4', '741.71', '2966.84', '2024-07-17'),
('45', 'Jonathan Edwards', 'Smartphone', '3', '406.39', '1219.17', '2025-03-03'),
('46', 'Laurie Daniels', 'Mouse', '3', '301.11', '903.33', '2024-05-17'),
('47', 'Sara Erickson', 'Keyboard', '2', '592.07', '1184.14', '2024-12-03'),
('48', 'John Stone', 'Headphones', '1', '1045.21', '1045.21', '2024-08-03'),
('49', 'Robert Reynolds', 'Mouse', '3', '1246.72', '3740.16', '2024-04-28'),
('50', 'Sheryl Simmons', 'Laptop', '2', '484.12', '968.24', '2024-10-16'),
('51', 'Misty Rodgers', 'Mouse', '5', '1418.65', '7093.25', '2024-05-07'),
('52', 'Timothy Jones', 'Laptop', '3', '1061.68', '3185.04', '2025-03-28'),
('53', 'David Wheeler', 'Keyboard', '1', '1179.82', '1179.82', '2024-10-05'),
('54', 'Jennifer Rosales', 'Headphones', '4', '221.66', '886.64', '2025-01-11'),
('55', 'Robert Anderson', 'Monitor', '2', '1204.04', '2408.08', '2024-11-17'),
('56', 'Christina Shepard', 'Mouse', '5', '1222.58', '6112.9', '2024-05-04'),
('57', 'Tyler Graves', 'Monitor', '2', '314.84', '629.68', '2025-04-24'),
('58', 'Melissa Simpson', 'Keyboard', '4', '79.11', '316.44', '2024-06-20'),
('59', 'Brian Morse', 'Smartphone', '2', '938.53', '1877.06', '2024-08-31'),
('60', 'Laura Walsh', 'Mouse', '1', '1099.72', '1099.72', '2024-06-14'),
('61', 'Chase Nelson', 'Keyboard', '2', '900.07', '1800.14', '2025-02-25'),
('62', 'Brian Flores', 'Smartphone', '5', '1006.22', '5031.1', '2024-11-23'),
('63', 'David Hernandez', 'Smartphone', '3', '230.77', '692.31', '2024-05-28'),
('64', 'Susan Cook', 'Keyboard', '4', '392.74', '1570.96', '2024-06-05'),
('65', 'Daniel Hooper', 'Laptop', '4', '1386.1', '5544.4', '2024-11-06'),
('66', 'Jessica Espinoza', 'Smartphone', '5', '855.36', '4276.8', '2025-01-01'),
('67', 'Joseph Tucker', 'Headphones', '2', '626.22', '1252.44', '2024-08-29'),
('68', 'Tyler Castillo', 'Smartphone', '3', '1344.75', '4034.25', '2024-07-11'),
('69', 'Timothy Chambers', 'Mouse', '5', '580.24', '2901.2', '2024-05-13'),
('70', 'Jeffery Mccoy', 'Keyboard', '5', '455.33', '2276.65', '2024-05-24'),
('71', 'Raven Copeland', 'Headphones', '3', '334.09', '1002.27', '2024-12-06'),
('72', 'Pamela Rowe MD', 'Headphones', '2', '512.61', '1025.22', '2024-06-09'),
('73', 'Craig Pierce', 'Keyboard', '5', '425.08', '2125.4', '2025-04-23'),
('74', 'Daniel Turner', 'Monitor', '3', '1036.87', '3110.61', '2024-11-13'),
('75', 'Russell Ware Jr.', 'Smartphone', '4', '708.7', '2834.8', '2024-06-07'),
('76', 'Jacob Johnson', 'Monitor', '2', '829.36', '1658.72', '2024-09-16'),
('77', 'Erin Castro', 'Headphones', '2', '829.93', '1659.86', '2025-04-06'),
('78', 'Colleen Hansen', 'Mouse', '4', '316.28', '1265.12', '2024-12-27'),
('79', 'Jackie Reid', 'Mouse', '3', '111.37', '334.11', '2024-08-20'),
('80', 'Jose Stein', 'Laptop', '1', '1305.64', '1305.64', '2024-05-27'),
('81', 'Steven Davis', 'Monitor', '3', '1285.55', '3856.65', '2024-11-06'),
('82', 'Franklin King PhD', 'Keyboard', '2', '188.74', '377.48', '2024-10-16'),
('83', 'Taylor Sharp', 'Laptop', '4', '53.53', '214.12', '2025-02-16'),
('84', 'Lee Davenport', 'Laptop', '3', '141.49', '424.47', '2024-11-27'),
('85', 'Diamond Wood', 'Mouse', '2', '984.92', '1969.84', '2024-07-06'),
('86', 'Carlos Smith', 'Laptop', '1', '869.48', '869.48', '2024-05-27'),
('87', 'Joseph Stanton', 'Keyboard', '4', '511.77', '2047.08', '2025-01-06'),
('88', 'Anna Walsh', 'Monitor', '1', '1310.31', '1310.31', '2025-03-18'),
('89', 'Thomas Tucker', 'Smartphone', '4', '326.97', '1307.88', '2024-07-05'),
('90', 'Roger Mccoy', 'Mouse', '1', '472.47', '472.47', '2025-04-19'),
('91', 'Daniel Jensen', 'Keyboard', '4', '664.84', '2659.36', '2024-07-17'),
('92', 'Brianna Irwin', 'Keyboard', '4', '619.83', '2479.32', '2024-12-02'),
('93', 'Jennifer Mccoy', 'Headphones', '1', '730.36', '730.36', '2024-09-30'),
('94', 'Jonathan Hart', 'Smartphone', '5', '785.0', '3925.0', '2024-12-18'),
('95', 'Teresa Ramos', 'Laptop', '1', '1126.81', '1126.81', '2025-04-24'),
('96', 'Rodney Conner', 'Keyboard', '4', '77.67', '310.68', '2024-07-14'),
('97', 'Toni Gray', 'Monitor', '3', '662.74', '1988.22', '2025-02-06'),
('98', 'Stephen Ellis', 'Monitor', '1', '542.12', '542.12', '2024-09-01'),
('99', 'Danielle Rich', 'Monitor', '2', '393.27', '786.54', '2024-07-19'),
('100', 'Erin Bates', 'Smartphone', '4', '352.35', '1409.4', '2024-10-05'),

]

cursor.executemany("INSERT INTO sales(id, customer, product, quantity, unit_price, total_price, sale_date) VALUES (?, ?, ?, ?, ?, ?, ?)", data)
conn.commit()

query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * unit_price) AS revenue 
FROM sales
GROUP BY product
"""

cursor.execute(query)
results = cursor.fetchall()

print("Product\tTotal Qty\tRevenue\n")
for row in results:
    print("{:<12}, {:<10}, {:<12.2f}".format(row[0],row[1],row[2]))

with open("sales_summary.txt", "w") as f:
    f.write(f"{'Product':<12} {'Total Qty':<10} {'Revenue':<12}\n")
    for row in results:
        f.write(f"{row[0]:<12}\t{row[1]:<10}\t\t{row[2]:<12.2f}\n")
