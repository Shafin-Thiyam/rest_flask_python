import sqlite3

class ItemModel:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def findByName(cls, name):
        con = sqlite3.connect('data.db')
        cursor = con.cursor()
        query = "select * from Item where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        con.close()
        if row:
            return cls(*row)

    def insert(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        i_query = "insert into Item values(?, ?)"
        cur.execute(i_query, (self.name, self.price))
        con.commit()
        con.close()


    def update(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        u_query = "update Item set price=? where name=?"
        cur.execute(u_query, (self.price, self.name))
        con.commit()
        con.close()

