
from flask import render_template
from flask import request

from . import ui

import predix.data.dbaas

psql = predix.data.dbaas.PostgreSQL()

@ui.route('/')
def index():
    """
    Trivial little demo of a form with some bad UX.
    """
    msg = ''

    a = request.args.get('a') or ''
    b = request.args.get('b') or ''
    c = request.args.get('c') or ''
    if (a or b or c):
        res = psql.execute('INSERT INTO foo(a, b, c) VALUES(:a, :b, :c)',
                a=a, b=b, c=c)
        msg = 'Added new row'

    rs = psql.execute('SELECT * FROM foo')
    return render_template('index.html', rs=rs, msg=msg)
