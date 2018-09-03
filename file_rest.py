from flask import Flask,request
from flask_restful import Resource, Api
import os

hostnames=os.environ(['HOSTNAME'])

app=Flask(__name__)
api=Api(app)
@app.route("/upload", methods=["POST"])
def upload():
    out_data = {}
    uploaded_files = request.files.getlist("file[]")
    print (uploaded_files)
    out_data["content"]=uploaded_files
    return out_data["content"]

app.run(port=5000,debug=True)
