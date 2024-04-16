import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

cursor = db.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
value = ("Hafidz", "Samarinda")

cursor.execute(sql, value)
db.commit()

print("{} data inserted".format(cursor.rowcount))