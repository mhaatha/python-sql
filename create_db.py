import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_mainan")

print("Database successfully created!")