from imaplib import IMAP4_SSL

from imapinboxrules.model.imap import ImapMailbox
from imapinboxrules.exceptions.connector import ConnectorError

class ImapConnector:

  def __init__(self, **kwargs):
    self.connection = IMAP4_SSL(**kwargs)

  def login(self, **kwargs):
    self.connection.login(**kwargs)

  def list_mailbox(self, **kwargs):
    res, data = self.connection.list(**kwargs)

    if res == 'NO':
      raise ConnectorError(data)

    if data == [None]:
      return []

    return [ImapMailbox.from_bytes_with_connector(self, el) for el in data]
