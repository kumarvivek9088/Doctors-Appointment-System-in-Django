from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime,timedelta
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def evnt(patient,doctor,startime,speciality,doctoremail,patientemail):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        endtime = (datetime.strptime(startime,"%Y-%m-%dT%H:%M:%S") + timedelta(minutes=45)).strftime('%Y-%m-%dT%H:%M:%S')
        event = {
            'summary': f'{doctor}',
            'location': 'Banao hospital',
            'description': f'patient {patient} have appointment with you on speciality : - {speciality}',
            'start': {
                'dateTime': startime,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': endtime,
                'timeZone': 'Asia/Kolkata',
            },
            
            'attendees': [
                {'email': doctoremail},
                {'email': patientemail},
            ],
        }
        event = service.events().insert(calendarId='8b1b5af2cf7ef36b899b53133c7eacd2e843c612acaaf695c4d880bfc1d95d6f@group.calendar.google.com', body=event).execute()
        # print('Event created: %s' % (event.get('htmlLink')))
        print("event created")


    except HttpError as error:
        print('An error occurred: %s' % error)





