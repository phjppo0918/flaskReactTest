from flask import Blueprint
routes = Blueprint('routes', __name__)

from .imageController import *
from .jsonController import *
from .dbController import *
from .rabbitmqController import *