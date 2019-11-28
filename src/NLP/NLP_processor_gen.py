
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.NLP.dates_time_process import process_date_time
from src.Functions.Response_generator import Response_generator

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################


class NLP_processor:
    def __init__(self):
        # --> Initialise tools
        self.response_generator = Response_generator()
        self.date_tool = process_date_time()

    def process_text(self, text):
        # --> Format text
        text = text.lower()

        sentence_structure = {"text": text,
                              "nouns": [],
                              "pronouns": [],
                              "verbs": [],
                              "adjectives": [],
                              "adverbs": [],
                              "prepositions": [],
                              "conjunctions": [],
                              "date": None}

        # --> Check for dates in text
        sentence_structure["date"] = self.date_tool.get_date(text)

        # --> Generate response
        response = self.response_generator.generate_response(sentence_structure)
