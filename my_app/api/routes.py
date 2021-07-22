from flask import Blueprint, request, jsonify, redirect, send_file

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return send_file('../../test.txt')
    # return redirect('www.google.com')


# CREATEMOREROUTES