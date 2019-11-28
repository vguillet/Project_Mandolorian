
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs

# Own modules
from src.Functions.Queries.google_calendar_queries import Google_calendar_queries
import datetime

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################


def morning_update():
    calendar_query_tool = Google_calendar_queries()

    # --> Fetch update information
    current_time = str(datetime.datetime.today().time())



    # --> Construct morning update text
    text = "Good morning Victor. It is currently " + str(current_time[:2]) + " " + str(current_time[3:5])

    print(text)

if __name__ == "__main__":
    morning_update()