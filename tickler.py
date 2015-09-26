#!/usr/bin/python

import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from os.path import join
from datetime import *
import json
import dateutil.parser as dparser


# GLOBALS Settings
SUBJECT = "Tickler Files for {0}".format(datetime.now().strftime("%A, %b %d"))


def check_tickler_file(name):
    try:
        d = dparser.parse(name,fuzzy=True).date()
        if d == date.today():
            return True
        else:
            return False
    except:
        pass

output = []

def send_mail(output):
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = data['email']['from']
    msg['To'] = data['email']['to']
    for f in output:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(name))
        msg.attach(part)
    server = smtplib.SMTP_SSL(data['email']['host'],465)
    server.login(data['email']['username'], data['email']['password'])
    server.sendmail(data['email']['from'], data['email']['to'], msg.as_string())


with open('config.json') as json_data_file:
    data = json.load(json_data_file)


directory = data['other']['directory']


for root,dirs, files in os.walk(directory):
    for name in files:
        if (check_tickler_file(name)==True):
            f = join(root,name)
            output.append(f)
if output:
    send_mail(output)