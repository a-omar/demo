import psycopg2
import sys
import pprint

class Database:
    def __init__(self):
        self.conn_string = "host='localhost' dbname='postgres' user='omara' password='postgres'"

    def query(self, query_string):

        conn = psycopg2.connect(self.conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()

        # execute our Query
        cursor.execute(query_string)

        # retrieve the records from the database
        records = cursor.fetchone()

        # print out the records using pretty print
        # note that the NAMES of the columns are not shown, instead just indexes.
        # for most people this isn't very useful so we'll show you how to return
        # columns as a dictionary (hash) in the next example.
        return records[0]

class ShoppingCart:

    def __init__(self):
        self.Products = 0

    def get_products_db(self):
        db = Database()
        self.Products = db.query("select count(*) from cart")


    def remove_products(self,num):
        self.Products -= num

    def get_products(self):
        return self.Products

"""
db = Database()
val = db.query("select count(*) from cart")
print(val[0])
"""

cart = ShoppingCart()
cart.get_products_db()
cart.remove_products(1)
print(cart.get_products())
