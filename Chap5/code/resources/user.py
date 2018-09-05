import sqlite3
from flask_restful import Resource, reqparse
from models.user import UsersModel

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
        if(UsersModel.findByUserName(data['username'],)) is not None:
            return {"messaage":"Username already exists"},400

        #users=UsersModel(data['username'],data['password'])
        users = UsersModel(**data)# since data is key value pair we can implement **kwargs
        users.save_to_db()
        #con=sqlite3.connect('data.db')
        #cur=con.cursor()
        #query="insert into users values(NULL, ?, ?)"
        #cur.execute(query,(data['username'],data['password']))
        #con.commit()
        #con.close()
        return {"messaage":"User created successfully"},201
