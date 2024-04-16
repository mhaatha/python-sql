import mysql.connector
import os

db = mysql.connector.connect(
  host = "localhost",
  user = "<your_database_username>",
  password = "<your_database_password>",
  database = "toko_mainan"
)

def insert_data(db): 
  name = input("Masukkan nama: ")
  address = input("Masukkan alamat: ")
  value = (name, address)

  cursor = db.cursor()

  sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"

  cursor.execute(sql, value)

  db.commit()

  print("{} data ditambahkan".format(cursor.rowcount))

def show_data(db):
  cursor = db.cursor()

  sql = "SELECT * FROM Customers"

  cursor.execute(sql)

  results = cursor.fetchall()

  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def update_data(db):
  cursor = db.cursor()

  show_data(db)

  customer_id = input("Pilih id customer> ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE Customers SET name = %s, address = %s WHERE customer_id = %s"
  value = (name, address, customer_id)

  cursor.execute(sql, value)

  db.commit()

  print("{} data diubah".format(cursor.rowcount))

def delete_data(db):
  cursor = db.cursor()

  show_data(db)

  customer_id = input("Pilih id customer> ")

  sql = "DELETE FROM Customers WHERE customer_id = %s"
  value = (customer_id,)

  cursor.execute(sql, value)

  db.commit()

  print("{} data dihapus".format(cursor.rowcount))

def search_data(db):
  cursor = db.cursor()

  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM Customers WHERE name LIKE %s OR address LIKE %s"
  value = ("%{}%".format(keyword), "%{}%".format(keyword))

  cursor.execute(sql, value)
  results = cursor.fetchall()

  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert data")
  print("2. Tampilkan data")
  print("3. Update data")
  print("4. Hapus data")
  print("5. Cari data")
  print("0. Exit")
  print("-------------------------")

  menu = input("Pilih menu> ")

  # clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu(db)