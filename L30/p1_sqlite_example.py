import sqlite3
from pprint import pprint

connection = sqlite3.connect('dbs/vendors.db', isolation_level=None)
cursor = connection.cursor()

#data = cursor.execute("select * from Vendors;")
# print(data)
# print(data is cursor)

# for row in cursor.execute("select * from Vendors;"):
#     print(row)

# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# pprint(data)
# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# pprint(data)

# cursor.execute("select * from Vendors;")
# row1 = cursor.fetchone()
# print(row1)
# row2 = cursor.fetchone()
# print(row2)
# row3 = cursor.fetchone()
# print(row3)
# row4 = cursor.fetchone()
# print(row4)
# row5 = cursor.fetchone()
# print(row5)

# cursor.execute("select * from Vendors;")
# data1 = cursor.fetchmany(size=2)
# print(data1)
# print()
# data2 = cursor.fetchmany(size=2)
# print(data2)
# print()
# data3 = cursor.fetchmany(size=2)
# print(data3)

# deal = 12
# cursor.execute(f"select * from Vendors where deal >= {deal};")
# data = cursor.fetchall()
# pprint(data)

# cursor.execute("select * from Vendors where deal >= ? and price < ?;", (12, 20000))
# data = cursor.fetchall()
# pprint(data)

# cursor.execute("select * from Vendors where deal >= :deal and price < :price;", {'deal': 12, 'price': 20000})
# data = cursor.fetchall()
# pprint(data)

# cursor.execute("INSERT INTO Vendors (name, item, deal, price) VALUES ('James2', 'car', 23, 1000.23)")
# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# pprint(data)
# connection.commit()

# cursor.execute("INSERT INTO Vendors (name, item, deal, price) VALUES ('James3', 'car', 34, 10.23)")
# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# pprint(data)

# cursor.executemany("INSERT INTO Vendors (name, item, deal, price) VALUES (:name, :item, :deal, :price)", [
#     {"name": "Oksana", "item": "train", "deal": 245, "price": 4344.5},
#     {"name": "Oksana2", "item": "train2", "deal": 53, "price": 45555}
# ])
# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# pprint(data)

# cursor.executescript("""
# CREATE TABLE  data3 (
# 	data_id INTEGER PRIMARY KEY,
#    	data_value TEXT NOT NULL,
#    	data_size INTEGER
# );
# INSERT INTO data3 (data_value, data_size)
# VALUES
#    ('line1', 5),
#    ('1', 1),
#    ('Loooooooooooooooooooooooooond', 999);
#
# """)

with open('dbs/test_script.sql', 'r') as f:
    cursor.executescript(f.read())

if connection:
    cursor.close()
    connection.close()
