"""
This section create authorizations for google spreadsheets API and for gmail API
"""
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import Setup

SERVICE_ACCOUNTS_CREDS_PATH = Setup.SERVICE_ACCOUNTS_CREDS_PATH
OAUTH2CLIENT_IDS_CREDS_PATH = Setup.OAUTH2CLIENT_IDS_CREDS_PATH
GMAIL_TOKEN_PATH = Setup.GMAIL_TOKEN_PATH

# If modifying these scopes, delete the file token.pickle.
SCOPES_GMAIL = ['https://www.googleapis.com/auth/gmail.modify']
SCOPES_SHEETS = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

def get_service_gmail():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(GMAIL_TOKEN_PATH):
        with open(GMAIL_TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(OAUTH2CLIENT_IDS_CREDS_PATH, SCOPES_GMAIL)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(GMAIL_TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)

    return service


def get_service_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNTS_CREDS_PATH, SCOPES_SHEETS)
    client = gspread.authorize(creds)
    return client
