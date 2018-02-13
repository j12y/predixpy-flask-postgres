
from flask import jsonify
from flask.globals import request
from werkzeug.utils import secure_filename

import predix.data.dbaas

from . import api

psql = predix.data.dbaas.PostgreSQL()

@api.route('/dbaas', methods=['GET'])
def select_foo():
    rs = psql.execute('SELECT * FROM foo')
    return jsonify(rs)

@api.route('/dbaas', methods=['POST'])
def insert_foo():
    rs = psql.execute('INSERT INTO foo(a, b, c) VALUES(:a, :b, :c)',
            a=request.args.get('a') or '',
            b=request.args.get('b') or '',
            c=request.args.get('c') or '')

    return jsonify(rs)
