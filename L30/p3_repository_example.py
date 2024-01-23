"""
CREATE TABLE if not exists Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);
INSERT INTO Vendors (name, item, deal, price)
VALUES
   ('John', 'car', 4, 1000.23),
   ('Anna', 'airplanes', 17, 20000),
   ('James', 'bikes', 12, 15.45),
   ('Karl', 'helicopters', 52, 14500);
"""


# str()
# repr()

# import datetime
# now = datetime.datetime.now()
# print(str(now))
# print(repr(now))
import sqlite3


class Vendor:

    def __init__(self, name, item, deal, price):
        self.name = name
        self.item = item
        self.deal = deal
        self.price = price

    def __repr__(self):
        return f"Vendor({self.name}, {self.item}, {self.deal}, {self.price})"

    def get_vendor_attributes(self):
        return self.name, self.item, self.deal, self.price


class VendorRepository:

    def __init__(self, path_to_db):
        self._connection = sqlite3.connect(path_to_db, isolation_level=None)
        self._cursor = self._connection.cursor()
        self._cursor.execute('CREATE TABLE if not exists Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);')

    def get_all(self):
        self._cursor.execute('SELECT * FROM Vendors;')
        data = self._cursor.fetchall()
        return self._rows2objects(data)

    def get_vendors_with_price_higher_then(self, price):
        self._cursor.execute('SELECT * FROM Vendors WHERE price > ?;', (price,))
        data = self._cursor.fetchall()
        return self._rows2objects(data)

    def add_vendor(self, vendor: Vendor):
        self._cursor.execute("INSERT INTO Vendors (name, item, deal, price) VALUES (?, ?, ?, ?)", vendor.get_vendor_attributes())

    def close(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()

    def _row2object(self, row):
        return Vendor(*row[1:])

    def _rows2objects(self, rows):
        result = []
        for row in rows:
            result.append(self._row2object(row))
        return result


if __name__ == '__main__':
    vendor1 = Vendor('John', 'car', 4, 1000.23)

    vendor_repository = VendorRepository('class_vendors.db')
    print(vendor_repository.get_all())
    # vendor_repository.add_vendor(vendor1)
    # print(vendor_repository.get_all())

    #vendor_repository.add_vendor(Vendor('Anna', 'airplanes', 17, 20000))
    #vendor_repository.add_vendor(Vendor('James', 'bikes', 12, 15.45))

    print(vendor_repository.get_vendors_with_price_higher_then(1000))
    vendor_repository.close()
