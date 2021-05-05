import os
import pytest

from dotenv import load_dotenv

from imapinboxrules.model.imap import ImapMailbox
from imapinboxrules.connector import ConnectorFactory
from imapinboxrules.exceptions.model.imap import ImapMailNotLoaded

class TestClassImapMailbox:

  mailbox = None

  def setup_method(self):
    load_dotenv()

    connector = ConnectorFactory.get_connector('imap')(
      ssl=False,
      host=os.environ.get('TEST_IMAP_HOST'),
      port=os.environ.get('TEST_IMAP_PORT'))

    connector.login(
      user=os.environ.get('TEST_IMAP_USERNAME'),
      password=os.environ.get('TEST_IMAP_PASSWORD'))

    self.mailbox = ImapMailbox.from_bytes_with_connector(
      connector,
      b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    self.mailbox.select()

  def test_load(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[0]

    mail.load()

  def test_read_header(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[0]

    mail.load()

    assert mail.header("FROM") == "GitHub <noreply@github.com>"

  def test_read_header_not_load(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[0]

    with pytest.raises(ImapMailNotLoaded):
      mail.header("FROM")

  def test_read_body(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[0]

    mail.load()

    assert len(mail.body()) > 0

  def test_read_body_2(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[0]

    mail.load()

    assert len(mail.body("text/plain")) > 0
    assert len(mail.body("text/html")) > 0

  def test_read_body_not_load(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[0]

    with pytest.raises(ImapMailNotLoaded):
      mail.body()

  def test_read_body_multipart(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[1]

    mail.load()

    assert len(mail.body("text/plain")) > 0
    assert len(mail.body("text/html")) > 0

  def test_read_body_multipart_2(self):
    mail = self.mailbox.search_mail(charset=None, criterion=["ALL"])[2]

    mail.load()

    assert len(mail.body("text/plain")) > 0
    assert len(mail.body("text/html")) > 0
