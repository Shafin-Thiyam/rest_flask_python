from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store=StoreModel.findByName(name)
        if store:
            return store.json()
        return {'message': '{} store not found'.format(name)},404

    def post(self,name):
        if StoreModel.findByName(name):
            return {'message':'{} store already exists'.format(name)},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'Something went wrong'},500
        return store.json(),201


    def delete(self,name):
        store=StoreModel.findByName(name)
        if store:
            store.delete_from_db()

        return {'message':'{} record deleted'.format(name)}


class StoreList(Resource):
    def get(self):
        # Following is multiple way you get using sqlalchemy
        # option 1: return {'stores':[store.json() for store in StoreModel.query.all()]}
        # option 1:return {'Stores': list(map(lambda x:x.json(),StoreModel.query.all()))}
        return {'Stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
