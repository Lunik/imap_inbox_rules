import os
import imaplib
import email

from dotenv import load_dotenv

IMAP_FOLDER_DELIMITER="."
DATA_FOLDER=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/mails/")

load_dotenv()

M = imaplib.IMAP4(host=os.environ.get('TEST_IMAP_HOST'), port=os.environ.get('TEST_IMAP_PORT'))
M.login(os.environ.get('TEST_IMAP_USERNAME'), os.environ.get('TEST_IMAP_PASSWORD'))

M.create("GitHub")
M.create("GitHub{delim}CI".format(delim=IMAP_FOLDER_DELIMITER))
M.create("GitHub{delim}CI{delim}Actions".format(delim=IMAP_FOLDER_DELIMITER))
M.create("GitHub{delim}Wiki".format(delim=IMAP_FOLDER_DELIMITER))

for root, dirs, files in os.walk(DATA_FOLDER, topdown = False):
  mailbox = root.replace(DATA_FOLDER, '').replace('/', IMAP_FOLDER_DELIMITER)

  for mail_file in files:
    with open(os.path.join(root, mail_file), 'r') as f:
      mail = email.message_from_string(f.read())

      M.append(mailbox=mailbox, flags=None, date_time=None, message=bytes(mail))
