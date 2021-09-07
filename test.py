import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ServiceAccountCreds", default=["None"],
					nargs=1, help="Please Enter Service Account creds path")

args = parser.parse_args()


SCOPES_SHEETS = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


SERVICE_ACCOUNTS_CREDS_PATH = args.ServiceAccountCreds[0]
print("################################")
print(SERVICE_ACCOUNTS_CREDS_PATH)
print("################################")

def get_service_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNTS_CREDS_PATH, SCOPES_SHEETS)
    client = gspread.authorize(creds)
    return client
  
  
  
  
