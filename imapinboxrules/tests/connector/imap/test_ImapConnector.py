import pytest
import os

from dotenv import load_dotenv

from imapinboxrules.connector.imap import ImapConnector
from imapinboxrules.model.imap import ImapMailbox

class TestClassImapConnector:

  def setup_method(self, method):
    load_dotenv()

    self.connector = ImapConnector(host=os.environ.get('TEST_IMAP_HOST'))

    self.connector.login(
      user=os.environ.get('TEST_IMAP_USERNAME'),
      password=os.environ.get('TEST_IMAP_PASSWORD'))

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

    assert mailboxes[0].name == "GitHub"
    assert mailboxes[0].location == ""

    assert mailboxes[1].name == "CI"
    assert mailboxes[1].location == "GitHub"

    assert mailboxes[2].name == "Actions"
    assert mailboxes[2].location == "GitHub/CI"

  def test_list_mailbox_folder_pattern(self):
    mailboxes = self.connector.list_mailbox(directory="GitHub", pattern="*Wiki*")

    assert len(mailboxes) == 1

    assert mailboxes[0].name == "Wiki"
    assert mailboxes[0].location == "GitHub"

  def test_list_mailbox_invalid_folder(self):
    mailboxes = self.connector.list_mailbox(directory="INVALIDFOLDER")

    assert len(mailboxes) == 0

    assert mailboxes == []

  # TODO
  def test_list_mailbox_NO(self):
    mailboxes = self.connector.list_mailbox(directory="TODO")

    assert len(mailboxes) == 0

    assert mailboxes == []