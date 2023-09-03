from datetime import date
from send_email import send_email

import pandas as pd 
import certifi
import ssl
import requests

# Set SSL certificates for requests. not recommended for production use.
ssl._create_default_https_context = ssl._create_unverified_context

# public google sheets or excel url
# convert the file into csv format
SHEET_ID = "1Gq9ERrEABzw6Tc7gYvb7TeaSk7r0UrbCaMEjAUQNi6E" # find the id in url
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# load spreadsheet into pandas dataframe
def load_df(url):
    # tell pandas that column names should be converted into datetime object
    parse_dates = ["transferred_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)

    return df

print(load_df(URL))


# Use pandas to query data and send emails according to the criterias
def query_data_and_send_emails(df):
    present = date.today()

    # set an email counter for how many emails have we sent 
    email_counter = 0

    # let's do more with the reminder date
    # python will only send email if it is paid
    for _, row in df.iterrows():
        if (row["has_paid"] == "yes"): # (present <= row["reminder_date"].date())
            send_email(
                subject=f"{row['company']} Invoice: {row['invoice_no']}",
                receiver_email=row["email"],
                name=row["name"],
                transferred_date=row["transferred_date"].strftime("%d, %b %Y"),
                invoice_no=row["invoice_no"],
                amount=row["amount"],
            )
            email_counter += 1
    
    return f"Total emails sent: {email_counter}"


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)