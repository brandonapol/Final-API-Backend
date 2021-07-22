from flask import Blueprint, request, jsonify, redirect

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}
    # return redirect('www.google.com')


# CREATEMOREROUTES