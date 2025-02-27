import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList, Item
from resources.store import Store, StoreList

# create the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# create secret key
app.secret_key = 'steven'
# pass the app into the API
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

# tell the API that the Item resource is available from the API
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
