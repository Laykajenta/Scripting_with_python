import smtplib
from email.message import EmailMessage

email = EmailMessage()
email ['from'] = 'Marianne Ødegaard'
email['to']='marianne.odegaard@gmail.com'
email['subjet']= 'Du vant 1 million'

email.set_content('jeg kan python programmering')

with smtplib.SMTP(host='smtp.gmail.com.', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('talvikpython@gmail.com', 'TalvikFinnmark1')
    smtp.send_message(email)
    print('alt ok, sjef')