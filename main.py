import os
import base64
import quopri

from dotenv import load_dotenv

from imapinboxrules.connector import ConnectorFactory

load_dotenv()

#print(os.environ)

connector = ConnectorFactory.get_connector('imap')(ssl=False, host=os.environ.get('TEST_IMAP_HOST'), port=os.environ.get('TEST_IMAP_PORT'))

connector.login(
  user=os.environ.get('TEST_IMAP_USERNAME'),
  password=os.environ.get('TEST_IMAP_PASSWORD'))

mailboxes = connector.list_mailbox()

mailbox = mailboxes[1]

mailbox.select()

#for mail in mailbox.search_mail():
#  mail.load()
#  mail.header("Subject")
#  print(mail.body("text/html"))
#  print(mail.body("text/plain"))

mails = mailbox.search_mail()

mails[1].load()

#print(mails[1].body("text/html"))
print(mails[1].body("text/plain"))