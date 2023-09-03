from datetime import datetime
from send_email import send_email

import pandas as pd

# public google sheets or excel url
# convert the file into csv format
SHEET_ID = "1QoFLhYluHRStNlLUk6CMczRFtQrK9UY-ueRbenY3h1Q" # find the id in url
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"