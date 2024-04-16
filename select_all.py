import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

cursor = db.cursor()

sql = "SELECT * FROM Customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)