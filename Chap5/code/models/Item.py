import sqlite3
from db import db
from twisted.conch.test.test_session import session


class ItemModel(db.Model):
    __tablename__='Item'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id=db.Column(db.Integer, db.ForeignKey('Stores.id'))
    store=db.relationship('StoreModel')

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def findByName(cls, name):
        return cls.query.filter_by(name=name).first() # it same as select * from Item where name =name LIMIT 1
        #above code same as below line of code
        #con = sqlite3.connect('data.db')
        #cursor = con.cursor()
        #query = "select * from Item where name=?"
        #result = cursor.execute(query, (name,))
        #row = result.fetchone()
        #con.close()
        #if row:
        #    return cls(*row)

    def save_to_db(self):#since it will work for both insert and update we change the name to more generic
        #below code will work for both insert and update
        db.session.add(self)
        db.session.commit()
        # above code same as below line of code
        #con = sqlite3.connect('data.db')
        #cur = con.cursor()
        #i_query = "insert into Item values(?, ?)"
        #cur.execute(i_query, (self.name, self.price))
        #con.commit()
        #con.close()

    #Since save_to_db will be used we no longer require update function
    #def update(self):
    #    con = sqlite3.connect('data.db')
    #    cur = con.cursor()
    #    u_query = "update Item set price=? where name=?"
    #    cur.execute(u_query, (self.price, self.name))
    #    con.commit()
    #    con.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

