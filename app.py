import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

# pip install pandas python-dotenv
from dotenv import load_dotenv

# Outlook port number and smtp server. This may varies depending on Mail Server that you use.
PORT = 587
EMAIL_SERVER = 'smtp-mail.outlook.com'


