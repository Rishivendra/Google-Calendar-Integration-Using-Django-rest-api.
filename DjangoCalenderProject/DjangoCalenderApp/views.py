from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from google.oauth2.credentials import Credentials
import google.auth
from googleapiclient.discovery import build

# Create a Django Rest Framework view to handle the /rest/v1/calendar/init/ endpoint:

@api_view(['GET'])
def GoogleCalendarInitView(request):
    # Step 1 of the OAuth flow
    # Prompt the user for his/her credentials
    # ...

    return Response({'message': 'OAuth flow initiated'})

# Create a Django Rest Framework view to handle the /rest/v1/calendar/redirect/ endpoint:
@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    # Handle the redirect request sent by Google with the code for the token

    # Get the access_token from the given code
    # ...

    # Use the access_token to get the list of events in the user's calendar
    credentials = Credentials.from_authorized_user_info(info=request.user)
    service = build('calendar', 'v3', credentials=credentials)
    calendar = service.calendars().get(calendarId='primary').execute()
    events = service.events().list(calendarId='primary', timeMin=time_min, maxResults=100, singleEvents=True, orderBy='startTime').execute()

    return Response({'events': events})

