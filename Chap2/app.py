from flask import Flask


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
     }
]
# End point for post /store data that will recieve is {name;}
@app.route("/store",methods=['POST'])
def create_store():
    pass

# End point for get /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    pass

# End point for get /store/
@app.route("/store")
def get_stores():
    pass

# End point for post /store/<string:name>/item{name:,price:,} data that will recieve is {name;}
@app.route("/store/<string:name>/item",methods=['POST'])
def create_item_in_store(name):
    pass

# End point for get /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    pass

@app.route("/")# for example www.google.com/ it represent the '/'
def Home():
    return "hello flask"

app.run(port=5000)