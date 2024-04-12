
from email.message import EmailMessage
import ssl
import smtplib
import requests
# import logging
from linode_api4 import LinodeClient, Instance





def notify_user_email(msg):
   EmailSender = 'gisooghafari@gmail.com'
   EmailPassword = 'muks zglj niwe qnuf'
   EmailReceiver = 'cabelucamelia@gmail.com'
   subject = 'There is a problem with your website!'
   msg = f'Subject: {subject}\n\n{msg}'

   em = EmailMessage()
   em['From'] = EmailSender
   em['To'] = EmailReceiver
   em['subject'] = subject
   em.set_content(msg)

   context = ssl.create_default_context()

   with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
           smtp.login(EmailSender, EmailPassword)
           smtp.sendmail(EmailSender, EmailReceiver, em.as_string())







def monitor_server():

    try:
        r = requests.get('https://digikala.com', timeout=5)

        if r.status_code != 200:
            # logging.info('Website is DOWN!')
            notify_user()
            reboot_server()
        else:
            # logging.info('Website is UP')
            pass  # Placeholder to maintain the structure
    except Exception as e:
        # logging.info('Website is DOWN!')
        notify_user_email()

