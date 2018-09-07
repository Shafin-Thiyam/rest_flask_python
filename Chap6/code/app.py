from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.item import Item, Itemlist
from resources.user import User_Register
from resources.store import Store, StoreList


app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
#for postgresql
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://ShafinHamna:admin@localhost/data'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.secret_key="jose"
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt=JWT(app,authenticate, identity)

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(Itemlist,'/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User_Register,'/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
