import imaplib
import re
import time

import html2text
from cryptography.fernet import Fernet
from imap_tools import MailBox, AND
from urllib.parse import urlparse, parse_qs
from datetime import datetime

from test.ui.utils.credentials import client_mail, client_password


class EmailClient:

    def __init__(self):
        self.login_to_mailbox()


    def login_to_mailbox(self):
        username = Fernet(client_mail['key']).decrypt(client_mail['code']).decode()
        password = Fernet(client_password['key']).decrypt(client_password['code']).decode()
        self.mailbox = MailBox('imap.gmail.com').login(username, password)
        print('Logged in to mailbox...')


    def get_email_as_html(self, receiver_email, subject, label='noreply',
                                 date_str=datetime.now().strftime('%Y-%m-%d')):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            self.mailbox.folder.set(label)
            messages = list(self.mailbox.fetch(AND(date_gte=date_obj, subject=subject, to=receiver_email)))

            try:
                last_message = messages[-1]
            except Exception:
                print('No emails matching the criteria.')
                return None

            plain_text = last_message.text
            if last_message.html:
                plain_text = html2text.html2text(last_message.html)

            plain_text = plain_text.replace('\r', '').replace('\n', '')
            link_regex = r'\[(.*?)\]\((.*?)\)'
        except:
            print()

        return plain_text.strip()



    def get_password_reset_token(self, receiver_email, subject, label='noreply',
                                 date_str=datetime.now().strftime('%Y-%m-%d'), link=False):
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            self.mailbox.folder.set(label)
            messages = list(self.mailbox.fetch(AND(date_gte=date_obj, subject=subject, to=receiver_email)))

            try:
                last_message = messages[-1]
            except Exception:
                print('No emails matching the criteria.')
                return None

            plain_text = last_message.text
            if last_message.html:
                plain_text = html2text.html2text(last_message.html)

            plain_text = plain_text.replace('\r', '').replace('\n', '')
            link_regex = r'\[(.*?)\]\((.*?)\)'

            for match in re.findall(link_regex, plain_text):
                if 'token' in match[1]:
                    parsed_url = urlparse(match[1])
                    query_params = parse_qs(parsed_url.query)
                    token = query_params.get('token', [None])[0]
                    if link:
                        return match[1]
                    print(f'Token found for user "{receiver_email}":', match[1])
                    return token

        except (imaplib.IMAP4.abort, Exception) as e:
            print('An error occurred in MailBox:', e)
            time.sleep(10)
            self.login_to_mailbox()


    def wait_to_get_password_reset_token(self, receiver_email, subject, max_try=25, link=False):
        for _ in range(max_try):
            token = self.get_password_reset_token(receiver_email, subject, link=link)
            if token is None:
                print(f'Password reset token is not found for "{receiver_email}"!')
                time.sleep(5)
            else:
                return token