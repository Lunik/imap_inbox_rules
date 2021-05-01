from imaplib import IMAP4_SSL,IMAP4

from imapinboxrules.model.imap import ImapMailbox
from imapinboxrules.exceptions.connector import ConnectorError
from imapinboxrules.exceptions.mailbox import MailboxNotFound, MailboxCheckFailed
from imapinboxrules.exceptions.model.imap import ImapMailNotFound

class ImapConnector:

  def __init__(self, ssl=True, **kwargs):
    if ssl:
      self.connection = IMAP4_SSL(**kwargs)
    else:
      self.connection = IMAP4(**kwargs)

  # https://tools.ietf.org/html/rfc3501#section-6.2.3
  def login(self, **kwargs):
    self.connection.login(**kwargs)

  # https://tools.ietf.org/html/rfc3501#section-6.3.8
  def list_mailbox(self, **kwargs):
    res, data = self.connection.list(**kwargs)

    if res == 'NO':
      raise ConnectorError(data)

    if data == [None]:
      return []

    return [ImapMailbox.from_bytes_with_connector(self, el) for el in data]

  # https://tools.ietf.org/html/rfc3501#section-6.3.1
  def select_mailbox(self, **kwargs):
    res, data = self.connection.select(**kwargs)

    if res == 'NO':
      if 'NONEXISTENT' in data[0].decode():
        raise MailboxNotFound(kwargs['mailbox'])

      raise ConnectorError(data)

    mail_count = data[0].decode()

    res, data = self.connection.check()

    if res == 'NO':
      raise MailboxCheckFailed(kwargs['mailbox'], data)

    return mail_count

  # https://tools.ietf.org/html/rfc3501#section-6.4.4
  def search_mail(self, charset, *args):
    res, data = self.connection.search(charset, *args)

    if res == 'NO':
      raise ConnectorError(data)

    if data == [None]:
      return []

    if data == [b'']:
      return []

    return data[0].decode().split(' ')

  # https://tools.ietf.org/html/rfc3501#section-6.4.5
  def fetch_mail(self, message_set, message_parts):
    res, data = self.connection.fetch(message_set, message_parts)

    if res == 'NO':
      raise ConnectorError(data)

    if data == [None]:
      raise ImapMailNotFound(message_set)

    return data[0][1]
