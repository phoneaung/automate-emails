import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

# pip install python-dotenv
from dotenv import load_dotenv

# outlook port number and smtp server. This may varies depending on Mail Server that you use. Adjust port if you use SSL.
PORT = 587
EMAIL_SERVER = 'smtp-mail.outlook.com'

# load the environment variables from .env file 
# included the if statement so that it will also work in Jupyter Notebook
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# read the environment variables
sender_email = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # create email msg
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Phone Aung", f"{sender_email}"))
    msg["To"] = receiver_email

    # add BCC and CC

    msg.set_content(
        f"""\
        Hi {name},
        I hope this email finds you well.
        I would like to remind you that MMK {amount} in invoice {invoice_no} is due for payment on {due_date}.
        Thank you and please let me know if you have any concerns.
        Best Regards,
        Phone Aung
        """
    )

    # add HTML version
    msg.add_alternative(
        f"""\
        <html>
            <body>
                <p>Hi {name},</p>
                <p>I hope this email finds you well.</p>
                <p>I would like to remind you that <strong>MMK {amount}</strong> in invoice {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
                <p>Thank you and please let me know if you have any concerns.</p>
                <p>Best Regards,</p>
                <p>Phone Aung</p>
            </body>
        </html> 
        """, 
        subtype="html",
    )