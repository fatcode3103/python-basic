import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root123@",
  database="demo_python_connect_db"
)

# Tạo một đối tượng cursor
# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("123", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# sql = "SELECT * FROM customers WHERE address LIKE '%le%' ORDER BY name DESC"
# sql = "DELETE FROM customers WHERE address = 'Blue Village'"
# sql = "UPDATE customers SET address = 'Green Grass 100' WHERE address = 'Green Grass 1'"

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

# mydb.commit()

myresult = mycursor.fetchall()  

for x in myresult:
  print(x)
