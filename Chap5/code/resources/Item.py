from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3
from models.Item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank'
                        )
    @jwt_required()
    def get(self,name):
        item=ItemModel.findByName(name)
        if item:
            return item.json()

        return {'Message':'Item not found'},404

    def delete(self,name):
        con=sqlite3.connect('data.db')
        cur=con.cursor()
        s_query="select * from Item where name=?"
        d_query="delete from Item where name=?"
        res=cur.execute(d_query,(name,))
        con.commit()
        con.close()
        return {'Message':'item deleted'}

    def put(self,name):
        getdata=Item.parser.parse_args()
        updated_item = ItemModel(name,getdata['price'])
        item=ItemModel.findByName(name)
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"Message":"Error occured while inserting the item."},500 # internal server error status code not a code issue
        else:
            try:
                updated_item.update()
            except:
                return {"Message":"Error occured while updating the item."},500 # internal server error status code not a code issue
        return updated_item.json()

    def post(self,name):
        if ItemModel.findByName(name):
            return {'Message':'An item with name {} already exists'.format(name)},400 # something went wrong
        data=Item.parser.parse_args()
        item=ItemModel(name,data['price'])

        try:
            item.insert()
        except:
            return {"Message":"Error occured while inserting the item."},500 # internal server error status code not a code issue

        return item.json(),201 #201 is for created

class Itemlist(Resource):

    def get(self):
        con= sqlite3.connect('data.db')
        cur=con.cursor()
        a_query="select * from Item"
        result=cur.execute(a_query)
        rows=result.fetchall()
        items=[]
        for row in rows:
            items.append({'item':{'name':row[0],'price':row[1]}})
        con.close()
        return {'items':items}

