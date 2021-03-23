from flask import Blueprint
from flask_restful import Api
from resources.health import Health
from resources.get_entities import NLPEntities

api_bp = Blueprint('api',__name__)
api = Api(api_bp)

# Route Configuration
api.add_resource(Health, '/Health')
api.add_resource(NLPEntities,'/Entities')
