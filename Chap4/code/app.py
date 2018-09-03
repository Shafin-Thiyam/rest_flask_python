from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
import Item
from user import User_Register


app=Flask(__name__)
app.secret_key="jose"
api=Api(app)
jwt=JWT(app,authenticate, identity)





api.add_resource(Item.Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(Item.Itemlist,'/items')
api.add_resource(User_Register,'/register')

if __name__=='__main__':
    app.run(port=5000,debug=True)
