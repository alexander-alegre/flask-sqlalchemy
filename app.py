import os

from flask import Flask, send_from_directory, render_template
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
# from create_tables import create_tables_if_not_exists


app = Flask(__name__, template_folder='client/build',
            static_folder="client/build/static")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'alex'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

# this was to create the migrations of tables ourselves
# create_tables_if_not_exists()

# Serve React App


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("client/build/" + path):
        return send_from_directory('client/build', path)
    else:
        return render_template('index.html')


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
