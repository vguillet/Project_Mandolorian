
##################################################################################################################
"""
This class handle all Google_calendar-related queries
"""

# Built-in/Generic Imports
import datetime
import pickle
import os
import os.path

# Libs
import pytz
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################


class Google_calendar_queries:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        self.service = self.__authenticate_google()

    def generate_response(self, day):

        # --> Fetch events from calendar
        events = self.__fetch_date_events(day)

        # --> Generate response accordingly
        if not events:
            return "No upcoming events found."
        else:
            response = "You have " + str(len(events)) + " events on this day. "

            # --> Generate events recap
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])

                # --> Get event starting hour
                start_time = str(start.split("T")[1].split("-")[0])
                if int(start_time.split(":")[0]) < 12:  # if the event is in the morning
                    start_time = start_time + "am"
                else:
                    start_time = str(int(start_time.split(":")[0]) - 12)  # convert 24 hour time to regular
                    start_time = start_time + "pm"

                response += event["summary"] + " at " + start_time

        return response

    def __fetch_date_events(self, day):
        # --> Reformat day to matching date format
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end = end.astimezone(utc)

        # --> Fetch events from the Google Calendar API
        events_result = self.service.events().list(calendarId='primary',
                                                   timeMin=date.isoformat(),
                                                   timeMax=end.isoformat(),
                                                   singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        return events

    def __authenticate_google(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        credentials = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                credentials = pickle.load(token)
    
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scopes)
                credentials = flow.run_local_server(port=0)
    
            with open('token.pickle', 'wb') as token:
                pickle.dump(credentials, token)
    
        service = build('calendar', 'v3', credentials=credentials)
    
        return service


if __name__ == "__main__":
    query_tool = Google_calendar_queries()
    query_tool.generate_response()
