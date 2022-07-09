import flask_cors
from flask import Flask
from routes import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)



# app.register_blueprint(imageController, url_prefix='/image')
app.register_blueprint(routes)

flask_cors.CORS(app, expose_headers='Authorization')

if __name__ == '__main__':
    app.run()

