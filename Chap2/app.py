from flask import Flask, jsonify, request, render_template
import xml2xml

app=Flask(__name__)
#post is to recieve data
#get is used to send data

stores=[
    {'name':'My wonderful store',
      'items':[
                {
                    'names':'My item',
                    'price':23
                }
     ]
     },
    {'name':'My wonderful store 2',
      'items':[
                {
                    'names':'My item 2',
                    'price':34
                }
     ]
     }
]
# End point for post /store data that will recieve is {name;}
@app.route("/store",methods=['POST'])
def create_store():
    request_data= request.get_json()
    new_store={'name': request_data['name'],'items':[]}
    stores.append(new_store)
    return jsonify(new_store)

# End point for get /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for i in stores:
        if i['name']==name:
            return jsonify(i)
    return jsonify({'Message':'Store not found'})



# End point for get /store/
@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})

# End point for post /store/<string:name>/item{name:,price:,} data that will recieve is {name;}
@app.route("/store/<string:name>/item",methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for i in stores:
        if i['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price'],
            }
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)

@app.route("/xmltransformer/<string:inputs>")
def get_xml(inputs):
    print("processing started...")
    xm2xm=xml2xml.xml_processsing('test.xsl',inputs)
    xm2xm.tranformation()
    print("processing Complete.")

# End point for get /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for i in stores:
        if i['name']==name:
            return jsonify({'items':i['items']})
    return jsonify({'Message':'Store not found'})

@app.route("/")# for example www.google.com/ it represent the '/'
def Home():
    return  render_template('index.html')

app.run(port=5000)