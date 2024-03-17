import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# Define the constants
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
TOKEN_PICKLE_FILE = "token.pickle"


def load_or_refresh_credentials():
    # Try to load stored credentials from file
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token_file:
            creds = pickle.load(token_file)
        # If credentials are expired, refresh them
        if creds and creds.expired:
            creds.refresh(Request())
        return creds
    return None


# Load or refresh credentials
creds = load_or_refresh_credentials()

# If credentials are not available or expired, initiate OAuth flow
if not creds:
    # Create a flow object
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', scopes=SCOPES)
    # Use the flow object to get credentials
    port = 8080  # Set the port to a fixed number
    creds = (flow.run_local_server(port=port))
    # Store the obtained credentials securely
    with open("token.pickle", "wb") as token_file:
        pickle.dump(creds, token_file)
    print("Access token obtained and stored successfully.")
else:
    print("Access token loaded successfully")

# Build the service
service = build('sheets', 'v4', credentials=creds)

# Define the spreadsheet ID and the new sheet name
spreadsheet_id = ""
new_sheet_name = 'Apr 24'

# Create a new sheet request
body = {
    'requests': [{
        'addSheet': {
            'properties': {
                'title': new_sheet_name
            }
        }
    }]
}

# Execute the request
response = service.spreadsheets().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body=body
).execute()

print(response)
