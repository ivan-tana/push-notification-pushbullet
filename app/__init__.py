from flask import Flask
from flask_restful import Api
app = Flask(__name__)


api = Api(app)

from .resources.resource import PushNote, PushLink

api.add_resource(PushNote, '/pushnote')
api.add_resource(PushLink, '/pushlink')
