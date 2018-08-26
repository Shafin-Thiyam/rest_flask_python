from flask_restful import Resource,Api,reqparse
from flask import Flask,request
from flask_jwt import JWT,jwt_required


items=[]

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank'
                        )
    @jwt_required()
    def get(self,name):
        #for item in items:
            #item=list(filter(lambda x: x['name']==name, items))  though list will give list of item but in this case we have single item so better to use 'next'
            # next give first item found by the filter function.
            #next function will throw error if no item is found so we add more parameter as 'None' which is returned when no item is found.
        item=next(filter(lambda x: x['name']==name, items),None)

            #if item['name']==name:
        return {'item':item}, 200 if item is not None else 400
        #return {"Item" :'none'},404 #404 status code os for file not found and most common status code is 200 which is for 'ok'

    def delete(self,name):
        global items #global inform python interpreter that items variable is not refering to local
                     # but outer and main variable declared initially
        items=list(filter(lambda x : x['name']!=name,items))
        return {'Message':'item deleted'}

    def put(self,name):
        #getdata=request.get_json()
        getdata=Item.parser.parse_args()
        #print(getdata['another']) it will throw error since another is not present and even if
        #add another in payload it will be erased since we are only parsing price

        item=next(filter(lambda x:x['name']==name,items),None)
        if item is None:
            item = {'name': name, 'price': getdata['price']}
            items.append(item)
        else:
        # this will not only update item price but also name in case
        #  slight change name. Since we are sending entire json payload
        # flask-restful has intersting option called reqparse to be included in import
            item.update(getdata)


        return item



    def post(self,name):

        if next(filter(lambda x:x['name']==name,items),None) is not None:
            return {'Message':"Item with name {} is already present".format(name)}, 400 # 400 is for bad request status

        data=Item.parser.parse_args()

        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201 #201 is for created

class Itemlist(Resource):

    def get(self):
        return {'items':items}

