import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import gspread
from oauth2client.service_account import ServiceAccountCredentials


PATH_TO_GMAIL_TOKEN = "/home/maor_animals_now_org/pytest/token.pickle"
PATH_TO_OAUTH2CLIENT_IDS_CREDS = "/home/maor_animals_now_org/pytest/credentials-OAuth2ClientIDs.json"
PATH_TO_SERVICE_ACCOUNTS_CREDS = "/home/maor_animals_now_org/pytest/credentials-ServiceAccounts.json"



# If modifying these scopes, delete the file token.pickle.
SCOPES_GMAIL = ['https://www.googleapis.com/auth/gmail.modify']

def get_service_gmail():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(PATH_TO_GMAIL_TOKEN):
        with open(PATH_TO_GMAIL_TOKEN, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(PATH_TO_OAUTH2CLIENT_IDS_CREDS, SCOPES_GMAIL)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(PATH_TO_GMAIL_TOKEN, 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)

    return service

SCOPES_SHEETS = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

def get_service_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(PATH_TO_SERVICE_ACCOUNTS_CREDS, SCOPES_SHEETS)
    client = gspread.authorize(creds)
    return client
