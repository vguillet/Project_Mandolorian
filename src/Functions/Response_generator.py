
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.Functions.Queries.google_calendar_queries import Google_calendar_queries

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################


class Response_generator:
    def __init__(self):
        self.triggers = {"calendar_queries_trigger": ["what do i have", "do i have plans", "am i busy"]}

    def generate_response(self, sentence_structure):
        response = None
        for key in self.triggers.keys():
            for trigger in self.triggers[key]:
                if trigger in sentence_structure["text"]:
                    response = Google_calendar_queries().generate_response(sentence_structure["date"])

        if response is None:
            return "Sorry, I could not process an adequate response"
        else:
            return response
