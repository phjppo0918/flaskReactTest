from flask_cors import CORS
from flask import Flask

from routes import *

app = Flask(__name__)

app.register_blueprint(routes)

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run()
