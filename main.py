import os

from dotenv import load_dotenv

from imapinboxrules.connector import ConnectorFactory

load_dotenv()

connector = ConnectorFactory.get_connector('imap')(host=os.environ.get('TEST_IMAP_HOST'))

connector.login(
  user=os.environ.get('TEST_IMAP_USERNAME'),
  password=os.environ.get('TEST_IMAP_PASSWORD'))

mailboxes = connector.list_mailbox()

for mailbox in mailboxes:
  print(mailbox.name)