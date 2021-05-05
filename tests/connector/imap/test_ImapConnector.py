import pytest
import os

from dotenv import load_dotenv

from imapinboxrules.connector.imap import ImapConnector
from imapinboxrules.model.imap import ImapMailbox
from imapinboxrules.exceptions.connector import ConnectorError
from imapinboxrules.exceptions.mailbox import MailboxNotFound
from imapinboxrules.exceptions.model.imap import ImapMailNotFound

class TestClassImapConnector:

  def setup_method(self, method):
    load_dotenv()

    self.connector = ImapConnector(ssl=False, host=os.environ.get('TEST_IMAP_HOST'), port=os.environ.get('TEST_IMAP_PORT'))

    self.connector.login(
      user=os.environ.get('TEST_IMAP_USERNAME'),
      password=os.environ.get('TEST_IMAP_PASSWORD'))

  def test_imap_connector_ssl(self):
    self.connector = ImapConnector(ssl=True, host="imap.gmail.com")

  def test_connector_connected(self):
    self.connector.connection.noop()

  def test_list_mailbox(self):
    mailboxes = self.connector.list_mailbox()

    assert len(mailboxes) > 0

    for mailbox in mailboxes:
      assert mailbox.__class__ is ImapMailbox

  def test_list_mailbox_folder(self):
    mailboxes = self.connector.list_mailbox(directory="GitHub")

    assert len(mailboxes) > 0

    assert mailboxes[0].name == "CI"
    assert mailboxes[0].location == "GitHub"

    assert mailboxes[1].name == "Actions"
    assert mailboxes[1].location == "GitHub.CI"

  def test_list_mailbox_folder_pattern(self):
    mailboxes = self.connector.list_mailbox(directory="GitHub", pattern="Wiki*")

    assert len(mailboxes) == 1

    assert mailboxes[0].name == "Wiki"
    assert mailboxes[0].location == "GitHub"

  def test_list_mailbox_invalid_folder(self):
    mailboxes = self.connector.list_mailbox(directory="INVALIDFOLDER")

    assert len(mailboxes) == 0

    assert mailboxes == []

  def test_select_mailbox(self):
    self.connector.select_mailbox(mailbox="GitHub")

  def test_select_mailbox_not_found(self):
    with pytest.raises(ConnectorError):
      self.connector.select_mailbox(mailbox="INVALIDFOLDER")

  def test_search_mail(self):
    self.connector.select_mailbox(mailbox="GitHub")
    
    mails = self.connector.search_mail(None, "ALL")

    assert mails == ['1', '2', '3']

  def test_search_mail_empty(self):
    self.connector.select_mailbox(mailbox="GitHub.Wiki")
    
    mails = self.connector.search_mail(None, "ALL")

    assert mails == []

  def test_fetch_mail(self):
    self.connector.select_mailbox(mailbox="GitHub")
    
    raw_mail = self.connector.fetch_mail("1", "(RFC822)")

    assert len(raw_mail) > 0

  def test_fetch_mail_notfound(self):
    self.connector.select_mailbox(mailbox="GitHub")
    
    with pytest.raises(ImapMailNotFound):
      self.connector.fetch_mail("99", "(RFC822)")