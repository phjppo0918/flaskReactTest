from flask import render_template
from . import routes
from flask import jsonify
from flask import make_response

class Test:
    def __init__(self):
        self.a1 = "asdf"
        self.a2 = 145

@routes.route('/json')
def getJson():
    data = Test()
    return jsonify(
        a1=data.a1,
        a2=data.a2,
        status=200
    )

@routes.route('/json/header')
def getJsonHeader():
    resp = make_response(jsonify(a = "asdf",
                                 b = 1234),
                         201)
    resp.headers['Content-Type'] = 'application/json'


    return resp
