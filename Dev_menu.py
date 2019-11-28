
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.Chat_bot.kortex_v1 import Kortex
from src.NLP.NLP_processor_gen import NLP_processor

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################

# --> Initialise tools
text_processor = NLP_processor()

# run = True
# while run is True:
chat_bot = Kortex(gender="male")
text = chat_bot.get_audio()
response = text_processor.process_text(text)


