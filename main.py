from datetime import datetime
from send_email import send_email

import pandas as pd 
import certifi

# Set SSL certificates for requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# public google sheets or excel url
# convert the file into csv format
SHEET_ID = "1QoFLhYluHRStNlLUk6CMczRFtQrK9UY-ueRbenY3h1Q" # find the id in url
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# load spreadsheet into pandas dataframe
def load_df(url):
    # tell pandas that column names should be converted into datetime object
    parse_dates = ["due_date", "reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)

    return df

print(load_df(URL))