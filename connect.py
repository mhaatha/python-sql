import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password;"
)

if db.is_connected():
  print("Successfully connect to the database!")