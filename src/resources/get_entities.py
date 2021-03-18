from flask import request,jsonify, Response, current_app as app
from flask_restful import Resource
from util.parser import Parser


class NLPEntities(Resource):

    def get(self):
        str_text = request.args.get('text')
        parse = Parser()
        nlp = app.nlp
        linker = app.linker
        doc = nlp(str_text)
        entity = doc.ents[1]
        entities = []
        nlp_entities = dict()

        for umls_ent in entity._.kb_ents:
            out = linker.kb.cui_to_entity[umls_ent[0]]
            val = parse.parse(out)
            entities.append(val.__dict__)
        nlp_entities['Entities'] = entities
        return nlp_entities


