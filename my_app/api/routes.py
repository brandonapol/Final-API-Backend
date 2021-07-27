from flask import Blueprint, request, jsonify, redirect, send_file
import shutil

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    # var_1 = request.args.get('yee')
    # print(var_1)
    # folder = os.listdir('/Users/brandonapol/Documents/coding_temple_rangers_63/this_is_the_end/final_flask_app/test.txt')
    # folder = os.path.join(folder, 'New Folder')
    my_zip = shutil.make_archive('my_zip', 'zip', '../template')
    # You need to go back and undo this!
    # #This works
    return send_file(my_zip, as_attachment=True)