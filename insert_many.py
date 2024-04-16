import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

cursor = db.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
values = [
  ("Doni", "Jakarta"),
  ("Ella", "Surabaya"),
  ("Fani", "Bandung"),
  ("Galih", "Depok")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data inserted".format(len(values)))