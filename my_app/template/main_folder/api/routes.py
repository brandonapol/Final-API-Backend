from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, User, Item, item_schema, items_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/items', methods = ['POST'])
@token_required
def create_item(current_user_token):
    name = request.json['name']
    description = request.json['description']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    item = Item(name, description, user_token = user_token )

    db.session.add(item)
    db.session.commit()

    response = item_schema.dump(item)
    return jsonify(response)

@api.route('/items', methods = ['GET'])
@token_required
def get_item(current_user_token):
    a_user = current_user_token.token
    items = Item.query.filter_by(user_token = a_user).all()
    response = items_schema.dump(items)
    return jsonify(response)

@api.route('/items/<id>', methods = ['GET'])
@token_required
def get_item_two(current_user_token, id):
    fan = current_user_token.token
    if fan == current_user_token.token:
        item = Item.query.get(id)
        response = item_schema.dump(item)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401

# UPDATE endpoint
@api.route('/items/<id>', methods = ['POST','PUT'])
@token_required
def update_item(current_user_token,id):
    item = Item.query.get(id) 
    item.name = request.json['name']
    item.description = request.json['description']
    item.user_token = current_user_token.token

    db.session.commit()
    response = item_schema.dump(item)
    return jsonify(response)


# DELETE car ENDPOINT
@api.route('/itemes/<id>', methods = ['DELETE'])
@token_required
def delete_item(current_user_token, id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    response = item_schema.dump(item)
    return jsonify(response)