from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
#import sqlite3
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank.'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item needs a store ID.'
                        )
    @jwt_required()
    def get(self,name):
        item=ItemModel.findByName(name)
        if item:
            return item.json()
        return {'Message':'Item not found'},404

    def delete(self,name):
        item=ItemModel.findByName(name)
        if item:
            item.delete_from_db()
        #con=sqlite3.connect('data.db')
        #cur=con.cursor()
        #s_query="select * from Item where name=?"
        #d_query="delete from Item where name=?"
        #res=cur.execute(d_query,(name,))
        #con.commit()
        #con.close()
        return {'Message':'item deleted'}

    def put(self,name):
        getdata=Item.parser.parse_args()
        items=ItemModel.findByName(name)
        #updated_item = ItemModel(name,getdata['price'])
        if items is None:
            #items=ItemModel(name,getdata['price'], getdata['store_id'])
            items = ItemModel(name, **getdata) # Same as above here we used **kwargs
            #try:
            #    updated_item.insert()
            #except:
            #    return {"Message":"Error occured while inserting the item."},500 # internal server error status code not a code issue
        else:
            items.price=getdata['price']
            #items.store_id=getdata['store_id']  Only do it if we want to update store id
            #try:
            #    updated_item.update()
            #except:
            #    return {"Message":"Error occured while updating the item."},500 # internal server error status code not a code issue
        items.save_to_db()
        return items.json()

    def post(self,name):
        if ItemModel.findByName(name):
            return {'Message':'An item with name {} already exists'.format(name)},400 # something went wrong
        data=Item.parser.parse_args()
        #item=ItemModel(name,data['price'],data['store_id'])
        item = ItemModel(name, **data) #same as above here we used **kwargs
        try:
            item.save_to_db()
        except:
            return {"Message":"Error occured while inserting the item."},500 # internal server error status code not a code issue

        return item.json()


class Itemlist(Resource):

    def get(self):
        #Following is multiple way you get using sqlalchemy
        # option 1: return {'item':[item.json() for item in ItemModel.query.all()]}
        # option 1:return {'item': list(map(lambda x:x.json(),ItemModel.query.all()))}
        return {'item': [item.json() for item in ItemModel.query.all()]}
        #con= sqlite3.connect('data.db')
        #cur=con.cursor()
        #a_query="select * from Item"
        #result=cur.execute(a_query)
        #rows=result.fetchall()
        #items=[]
        #for row in rows:
        #    items.append({'item':{'name':row[1],'price':row[2]}})
        #con.close()
        #return {'items':items}

