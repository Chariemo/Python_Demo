# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-06 9:11
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from_addr = input('From:')
passwd = input('PassWord:')
to_addr = input('To:')
# smtp_server = input('SMTP server:')
# port_smtp = int(input('SMTP_port:'))


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


server = smtplib.SMTP_SSL('smtp.163.com', 465)
# server.starttls()
server.set_debuglevel(1)
server.login(from_addr, passwd)

msg = MIMEMultipart()
msg['From'] = _format_addr('Python Leaner <%s>' % from_addr)
msg['To'] = _format_addr('Admin <%s>' % to_addr)
msg['Subject'] = Header('From SMTP...', 'utf-8').encode()

msg.attach(MIMEText('a text mail from python...', 'plain', 'utf-8'))

with open('C:\\Users\chenjianlin\Pictures\Aisi.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='Aisi.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='Aisi.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment_Id', '0')

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server.sendmail(from_addr, [to_addr], msg.as_bytes())
server.quit()
