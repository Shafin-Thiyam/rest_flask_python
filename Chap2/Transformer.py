import xml2xml
from flask import Flask
__author__='Shafin Thiyam'

app=Flask(__name__)


@app.route("/")
def welcome():
    print("Welcome to xmltransformer")



@app.route("/xmltransformer/<string:inputs>")
def get_xml(inputs):
    xm2xm=xml2xml.xml_processsing('Agency_Doc_Transformation.xsl',inputs)
    xm2xm.tranformation()

if __name__=='__main__':
    app.run(port=9090,debug=True)



