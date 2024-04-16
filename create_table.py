import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

cursor = db.cursor()

sql = """CREATE TABLE Customers
(
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
)"""

cursor.execute(sql)
print("Customers table successfully created!")