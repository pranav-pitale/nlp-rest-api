from flask import Flask, current_app
from app import api_bp
import spacy
from scispacy.linking import EntityLinker


def create_app(config_filename=None):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='/api')
    nlp = spacy.load("en_core_sci_sm")
    # This line takes a while, because we have to download ~1GB of data
    # and load a large JSON file (the knowledge base). Be patient!
    # Thankfully it should be faster after the first time you use it, because
    # the downloads are cached.
    # NOTE: The resolve_abbreviations parameter is optional, and requires that
    # the AbbreviationDetector pipe has already been added to the pipeline. Adding
    # the AbbreviationDetector pipe and setting resolve_abbreviations to True means
    # that linking will only be performed on the long form of abbreviations.
    nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})
    app.nlp = nlp
    app.linker = nlp.get_pipe("scispacy_linker")
    return app

if __name__ == "__main__":
    app = create_app('config')
