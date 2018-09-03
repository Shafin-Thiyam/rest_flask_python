import sqlite3
from flask_restful import Resource, reqparse
class Users:

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

class User_Register(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be left blank')
    def post(self):
        data=User_Register.parser.parse_args()
        if(Users.findByUserName(data['username'],)) is not None:
            return {"messaage":"Username already exists"},400

        con=sqlite3.connect('data.db')
        cur=con.cursor()
        query="insert into users values(NULL, ?, ?)"
        cur.execute(query,(data['username'],data['password']))
        con.commit()
        con.close()
        return {"messaage":"User created successfully"},201
