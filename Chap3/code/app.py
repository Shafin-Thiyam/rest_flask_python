from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import
import TestRestFul


app=Flask(__name__)
app.secret_key="haiqa"

api=Api(app)


api.add_resource(TestRestFul.Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(TestRestFul.Itemlist,'/items')

app.run(port=5000,debug=True)
