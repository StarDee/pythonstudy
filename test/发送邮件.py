# !/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
msg=MIMEText('hello,send by Python..','plain','utf-8')

from_addr=input('From:dixing2016@gmail.com')
password=input('Password:google24')

to_addr=input('To:707706247@qq.com')
smtp_server=input('SMTP server:smtp.gmail.com')

import smtplib
server=smtplib.SMTP(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,[to_addr],msg.as_string())
server.quit()