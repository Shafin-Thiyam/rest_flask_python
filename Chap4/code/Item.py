from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank'
                        )
    @classmethod
    def findByName(cls,name):
        con=sqlite3.connect('data.db')
        cursor=con.cursor()
        query="select * from Item where name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        con.close()
        if row:
            return {'item':{'name':row[0],'price':row[1]}},200

    @classmethod
    def insert(cls,item):
        con=sqlite3.connect('data.db')
        cur=con.cursor()
        i_query="insert into Item values(?, ?)"
        cur.execute(i_query,(item['name'],item['price']))
        con.commit()
        con.close()

    @classmethod
    def update(cls,item):
        con=sqlite3.connect('data.db')
        cur=con.cursor()
        u_query="update Item set price=? where name=?"
        cur.execute(u_query,(item['price'],item['name']))
        con.commit()
        con.close()


    @jwt_required()
    def get(self,name):
        item=self.findByName(name)
        if item:
            return item

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
        updated_item = {'name': name, 'price': getdata['price']}
        item=self.findByName(name)
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"Message":"Error occured while inserting the item."},500 # internal server error status code not a code issue
        else:
            try:
                self.update(updated_item)
            except:
                return {"Message":"Error occured while updating the item."},500 # internal server error status code not a code issue
        return updated_item

    def post(self,name):
        if self.findByName(name):
            return {'Message':'An item with name {} already exists'.format(name)},400 # something went wrong
        data=Item.parser.parse_args()
        item={'name':name,'price':data['price']}

        try:
            self.insert(item)
        except:
            return {"Message":"Error occured while inserting the item."},500 # internal server error status code not a code issue

        return item,201 #201 is for created

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

