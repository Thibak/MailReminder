# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 12:51:42 2014

@author: user
"""
import smtplib

from email.mime.text import MIMEText

#fp = open(textfile, 'rb')
# Create a text/plain message
#msg = MIMEText(fp.read())
#fp.close()


msg = 'aaa'
me = ''
you = ''
msg['Subject'] = 'Subject' 
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.gmail.com:587')
s.ehlo()
s.starttls()
s.login('', '')
s.sendmail(me, [you], msg.as_string())
s.quit()