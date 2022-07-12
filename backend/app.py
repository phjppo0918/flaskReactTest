from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from restfulTest import *

from routes import *

app = Flask(__name__)

app.register_blueprint(routes)

api = Api(app)
api.add_resource(Hello, '/rest')

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run()
