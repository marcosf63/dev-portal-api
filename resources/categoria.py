from flask_restful import Resource
from models.categoria import CategoriaModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "Store nao encontrada."}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Store '{}' ja existe.".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "Um erro cocorreu ao criar uma store"}, 500

        return store.json(), 201


    def delete(self, name):
       store = StoreModel.find_by_name(name)
       if store:
           store.delete_from_db()

       return {'message': "Store deletado com sucesso"}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}