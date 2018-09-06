import sqlite3
from db import db
class UsersModel(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username,password):
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findByUserName(cls,username):
        return cls.query.filter_by(username=username).first()
        #con= sqlite3.connect('data.db')
        #cursors=con.cursor()
        #select_q="select * from users where username=?"
        #result=cursors.execute(select_q,(username,))
        #row=result.fetchone()
        #if row is not None: same as below if condition
        #if row:
        #    #user=cls(row[0],row[1],row[2])
        #    #same as above
        #    user=cls(*row)
        #else:
        #    user=None
        #con.close()
        #return user

    @classmethod
    def findById(cls,_id):
        return cls.query.filter_by(id=_id).first()
        #con= sqlite3.connect('data.db')
        #cursors=con.cursor()
        #select_q="select * from users where id=?"
        #result=cursors.execute(select_q,(_id,))
        #row=result.fetchone()
        ##if row is not None: same as below if condition
        #if row:
            #user=cls(row[0],row[1],row[2])
            #same as above
            #user=cls(*row)
        #else:
        #    user=None
        #con.close()
        #return user

