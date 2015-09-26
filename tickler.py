import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from os.path import join
from datetime import datetime
import json
import dateutil.parser as dparser
from datetime import *


with open('config.json') as json_data_file:
    data = json.load(json_data_file)

SUBJECT = "Tickler Files for {0}".format(datetime.now().strftime("%A, %b %d"))
EMAIL_SERVER = data['email']['host']
EMAIL_FROM = data['email']['from']
EMAIL_TO = data['email']['to']

directory = data['other']['directory']

output = []
for root,dirs, files in os.walk(directory):
    for name in files:
        f = join(root,name)
        try:
            d = dparser.parse(name,fuzzy=True).date()
            print d
            if d == date.today():
                output.append(f)
        except:
            pass

if output:
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    for f in output:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(name))
        msg.attach(part)
    server = smtplib.SMTP_SSL(EMAIL_SERVER,465)
    server.login(data['email']['username'], data['email']['password'])
    server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())