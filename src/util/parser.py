from models.nlp_output import NLPOutput

class Parser:

    def parse(self, entities):
        nlp_output = NLPOutput()
        nlp_output.cui = entities.concept_id
        nlp_output.name = entities.canonical_name
        nlp_output.aliases = entities.aliases
        nlp_output.definition = entities.definition
        return nlp_output