import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('./index.html').read_text())

email = EmailMessage()
email ['from'] = 'Marianne Ødegaard'
email['to']='marianne.odegaard@gmail.com'
email['subjet']= 'Du vant 1 million'

email.set_content(html.substitute(name='TinTin'),'html')

with smtplib.SMTP(host='smtp.gmail.com.', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('talvikpython@gmail.com', 'olsh zfem dpgx suyl')
    smtp.send_message(email)
    print('alt ok, sjef')