import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import argparse
from AnimalsTestBot import emailfunc

parser = argparse.ArgumentParser()
parser.add_argument("--ServiceAccountCreds", default=["None"],
					nargs=1, help="Please Enter Service Account creds path")
parser.add_argument("--GmailToken", default=["/home/maor_animals_now_org/pytest/token.pickle"],
					nargs=1, help="Please Enter token.pickle path")
parser.add_argument("--Oauth2ClientCreds", default=["None"],
					nargs=1, help="Please Enter Oauth2Client creds path")

args = parser.parse_args()


SERVICE_ACCOUNTS_CREDS_PATH = args.ServiceAccountCreds[0]
OAUTH2CLIENT_IDS_CREDS_PATH = args.Oauth2ClientCreds[0]
GMAIL_TOKEN_PATH = args.GmailToken[0]

# SCOPES_SHEETS = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
#                  "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


# print("################################")
# print(SERVICE_ACCOUNTS_CREDS_PATH)
# print("################################")

# def get_service_sheet():
#     creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNTS_CREDS_PATH, SCOPES_SHEETS)
#     client = gspread.authorize(creds)
#     return client

# client = get_service_sheet()
# report_sheet = client.open("Report").sheet1
# print(report_sheet)


SCOPES_GMAIL = ['https://www.googleapis.com/auth/gmail.modify']


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

service = get_service_gmail()
message_text = "Just a small test"
sender = "me"
subject = "test"
to = "maor@animals-now.org"
user_id = "me"

message =  emailfunc.create_message(sender, to, subject, message_text)
emailfunc.send_message(service, user_id, message)
