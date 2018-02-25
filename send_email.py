# coding: utf-8
#!/usr/bin/env python

ard = serial.Serial('/dev/tty96B0', 115200)

# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
# Create a text/plain message
msg = MIMEText("Loud Noises Detected!")
msg['Subject'] = "Your DragonBoard has detected increased noise levels"
msg['From'] = "aTestEmail@gmail.com"
msg['To'] = "noiseReminder@gmail.com>"
# Send the message via our own SMTP server (sendmail)
s = smtplib.SMTP('localhost')
s.set_debuglevel(1)
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()
print "Email sent!"

