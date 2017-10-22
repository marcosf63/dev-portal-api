import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message" : "Item inexistente"}, 404
   
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])
        
        try:
            item.insert()
        except:
            return {'message': 'Um erro ocorreu ao inserir um item'}, 500

        return item.json(), 201
    
    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        item = ItemModel.find_by_name(name)

        if item is None:
            return {'message': "An item with name '{}' not exists.".format(name)}

        query = "DELETE FROM items WHERE name=?"
        try:
            cursor.execute(query, (name,))
        except:
            return {'message': 'Um erro ocorreu ao inserir um item'}, 500

        connection.commit()
        connection.close()

        return {'message': 'Item deletado.'}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {'message': 'Um erro ocorreu ao inserir um item'}, 500
        else:
            try:
                updated_item.update()
            except:
                return {'message': 'Um erro ocorreu ao atualizar um item'}, 500
        return updated_item.json()
 


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"

        result = cursor.execute(query)
        items = []

        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return { 'items': items}