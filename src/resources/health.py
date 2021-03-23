from flask import request,jsonify, Response 
from flask_restful import Resource

'''
Health Endpoint
'''
class Health(Resource):

    def get(self):
        return "I am healthy"