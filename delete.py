import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

cursor = db.cursor()

sql = "DELETE FROM Customers WHERE customer_id = %s"
value = (1,)

cursor.execute(sql, value)

db.commit()

print("{} data deleted".format(cursor.rowcount))