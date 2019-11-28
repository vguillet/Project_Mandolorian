
##################################################################################################################
"""
This class is used to obtain dates from text
"""

# Built-in/Generic Imports
import datetime

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################


class process_date_time:
    def __init__(self):
        self.keyword_dict = {"months": ["january", "february", "march", "april", "may", "june", "july",
                                        "august", "september", "october", "november", "december"],
                             "days": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
                             "day_extensions": ["rd", "th", "st", "nd"]}

    def get_date(self, text):

        today = datetime.date.today()

        # --> Return today's date if today is requested
        if text.count("today") > 0:
            return today

        # --> Return tomorrow's date if tomorrow is requested
        if text.count("tomorrow") > 0:
            return datetime.date.today() + datetime.timedelta(days=2)

        if text.count("the day after tomorrow") > 0:
            return datetime.date.today() + datetime.timedelta(days=1)

        # ----> Analyse text for key words and their values referred to through index
        # --> Initialise trackers
        day = None
        day_of_week = None
        month = None
        year = None

        for word in text.split():
            # --> Checking for month
            if word in self.keyword_dict["months"]:
                month = self.keyword_dict["months"].index(word)

            # --> Checking for day
            elif word in self.keyword_dict["days"]:
                day_of_week = self.keyword_dict["days"].index(word)

            # --> If digit is detected, assume it is a date reference
            elif word.isdigit():
                day = int(word)

            # --> Check if word consists of extension
            else:
                for ext in self.keyword_dict["day_extensions"]:
                    found = word.find(ext)
                    # --> If found, try converting previous part of word to digit and set as day
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass

        # --> Return none if no date found
        if year is None and month is None and day is None and day_of_week is None:
            return None

        # --> If month mentioned is before the current month and year is not specified, set year to the next
        if month is not None:
            if month < today.month and year is None:
                year = today.year + 1

        # --> If year not specified, set to this year
        if year is None:
            year = today.year

        # --> If day is specified but month isn't, set month to next
        if month is None and day is not None:
            if day < today.day:     # Assume day refers to next month
                month = today.month + 1
            else:                   # Assume day refers to this month
                month = today.month

        # --> If only day of the week specified
        if month is None and day is None and day_of_week is not None:
            current_day_of_week = today.weekday()
            dif = day_of_week - current_day_of_week

            if dif < 0:
                dif += 7
                if text.count("next") >= 1:
                    dif += 7

            return today + datetime.timedelta(dif)

        # --> If only day is specified
        if day is not None:
            print(month, day, year)
            print(datetime.date(day=day, month=month, year=year))
            return datetime.date(day=day, month=month, year=year)
