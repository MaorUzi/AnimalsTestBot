"""
This section manage all necessary files' path.
"""
import argparse

##### Default Paths #####
DEFAULT_CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
DEFAULT_SERVICE_ACCOUNTS_CREDS_PATH = "/home/maor_animals_now_org/pytest/credentials-ServiceAccounts.json"
DEFAULT_OAUTH2CLIENT_IDS_CREDS_PATH = "/home/maor_animals_now_org/pytest/credentials-OAuth2ClientIDs.json"
DEFAULT_GMAIL_TOKEN_PATH = "/home/maor_animals_now_org/pytest/token.pickle"
DEFAULT_ERROR_COUNTER_JSON_PATH = '/home/maor_animals_now_org/pytest/error_status.json'

parser = argparse.ArgumentParser()

parser.add_argument("--Chromedriver", default=[DEFAULT_CHROMEDRIVER_PATH],
					nargs=1, help="Please Enter chromedriver path")

parser.add_argument("--ServiceAccountCreds", default=[DEFAULT_SERVICE_ACCOUNTS_CREDS_PATH],
					nargs=1, help="Please Enter Service Account creds path")

parser.add_argument("--Oauth2ClientCreds", default=[DEFAULT_OAUTH2CLIENT_IDS_CREDS_PATH],
					nargs=1, help="Please Enter Oauth2Client creds path")

parser.add_argument("--GmailToken", default=[DEFAULT_GMAIL_TOKEN_PATH],
					nargs=1, help="Please Enter token.pickle path")

parser.add_argument("--ErrorCounter", default=[DEFAULT_ERROR_COUNTER_JSON_PATH],
					nargs=1, help="Please Enter error counter json file path")
parser.add_argument("--UtmTest", default=[''],
					nargs=1, help="Please Enter test utm parmeter value")

args = parser.parse_args()

##### Define the paths #####
CHROMEDRIVER_PATH = args.Chromedriver[0]
SERVICE_ACCOUNTS_CREDS_PATH = args.ServiceAccountCreds[0]
OAUTH2CLIENT_IDS_CREDS_PATH = args.Oauth2ClientCreds[0]
GMAIL_TOKEN_PATH = args.GmailToken[0]
ERROR_COUNTER_JSON_PATH = args.ErrorCounter[0]
UTM_TEST = args.UtmTest[0]


