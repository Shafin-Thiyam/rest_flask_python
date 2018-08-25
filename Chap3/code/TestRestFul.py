from flask_restful import Resource,Api
from flask import Flask,request
from flask_jwt import JWT,jwt_required


items=[]

class Item(Resource):
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

    @jwt_required()
    def post(self,name):

        if next(filter(lambda x:x['name']==name,items),None) is not None:
            return {'Message':"Item with name {} is already present".format(name)}, 400 # 400 is for bad request status

        data=request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item,201 #201 is for created

class Itemlist(Resource):
    @jwt_required()
    def get(self):
        return {'items':items}

