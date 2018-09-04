import sqlite3
class UsersModel:

    def __init__(self,_id, username,password):
        self.id=_id # we are using _id since id id is python reserverd keyword
        self.username=username
        self.password=password

    @classmethod
    def findByUserName(cls,username):
        con= sqlite3.connect('data.db')
        cursors=con.cursor()
        select_q="select * from users where username=?"
        result=cursors.execute(select_q,(username,))
        row=result.fetchone()
        #if row is not None: same as below if condition
        if row:
            #user=cls(row[0],row[1],row[2])
            #same as above
            user=cls(*row)
        else:
            user=None
        con.close()
        return user

    @classmethod
    def findById(cls,_id):
        con= sqlite3.connect('data.db')
        cursors=con.cursor()
        select_q="select * from users where id=?"
        result=cursors.execute(select_q,(_id,))
        row=result.fetchone()
        #if row is not None: same as below if condition
        if row:
            #user=cls(row[0],row[1],row[2])
            #same as above
            user=cls(*row)
        else:
            user=None
        con.close()
        return user

