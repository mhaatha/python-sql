import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

cursor = db.cursor()

sql = "UPDATE Customers SET name = %s, address = %s WHERE customer_id = %s"
value = ("Ardianta", "Lombok", 1)

cursor.execute(sql, value)

db.commit()

print("{} data diubah".format(cursor.rowcount))