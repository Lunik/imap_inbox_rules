import re

from imapinboxrules.utils.connector import require_connector

from .imap_mailbox_attributes import ImapMailboxAttributes
from .imap_mail import ImapMail

class ImapMailbox:

  connector = None

  location = ""
  delimiter = "/"
  full_path = ""

  has_children = False
  is_marked = False

  is_selectable = False

  is_draft = False
  is_sent = False
  is_spam = False
  is_trash = False

  def __init__(self, name):
    self.name = name

  @staticmethod
  def __parse_attributes(mailbox_attributes):
    return {
      'has_children': ImapMailboxAttributes.has_children(mailbox_attributes),
      'is_marked': ImapMailboxAttributes.is_marked(mailbox_attributes),
      'is_selectable': ImapMailboxAttributes.is_selectable(mailbox_attributes),
      'is_draft': ImapMailboxAttributes.is_draft(mailbox_attributes),
      'is_sent': ImapMailboxAttributes.is_sent(mailbox_attributes),
      'is_spam': ImapMailboxAttributes.is_spam(mailbox_attributes),
      'is_trash': ImapMailboxAttributes.is_trash(mailbox_attributes)
    }

  @staticmethod
  def __parse_path(delimiter, path):
    splitted = path.split(delimiter)

    return (splitted[-1], delimiter.join(splitted[0:-1]))

  @staticmethod
  def from_bytes(bytes):
    parsed = re.search(r'\((?P<attributes>[^)]*)\) "?(?P<delimiter>[^"]+)"? "?(?P<path>[^"]+)"?', bytes.decode())

    name, location = ImapMailbox.__parse_path(parsed.group('delimiter'), parsed.group('path'))

    imap_mailbox = ImapMailbox(name)
    imap_mailbox.location = location
    imap_mailbox.delimiter = parsed.group('delimiter')
    imap_mailbox.full_path = parsed.group('path')

    for attr, value in ImapMailbox.__parse_attributes(parsed.group('attributes')).items():
      setattr(imap_mailbox, attr, value)

    return imap_mailbox

  @staticmethod
  def from_bytes_with_connector(connector, bytes):
    mailbox = ImapMailbox.from_bytes(bytes)

    mailbox.connector = connector

    return mailbox

  @require_connector
  def list_mailbox(self, **kwargs):
    return self.connector.list_mailbox(directory=self.full_path, **kwargs)

  @require_connector
  def select(self, readonly=False):
    self.connector.select_mailbox(mailbox=self.full_path, readonly=readonly)

  @property
  @require_connector
  def count_mail(self):
    mails = self.connector.search_mail(None, "ALL")

    return len(mails)

  @require_connector
  def search_mail(self, charset=None, criterion=["ALL"]):
    mails = self.connector.search_mail(charset, *criterion)

    return [ImapMail.from_id_with_connector(self.connector, el) for el in mails]