import pytest
import os

from dotenv import load_dotenv

from imapinboxrules.model.imap import ImapMailbox
from imapinboxrules.connector import ConnectorFactory
from imapinboxrules.exceptions.model.imap import ImapMailboxWithoutConnector

class TestClassImapMailbox:

  def setup_method(self, method):
    load_dotenv()

    connector = ConnectorFactory.get_connector('imap')

    self.connector = connector(host=os.environ.get('TEST_IMAP_HOST'))

    self.connector.login(
      user=os.environ.get('TEST_IMAP_USERNAME'),
      password=os.environ.get('TEST_IMAP_PASSWORD'))

  def test_from_bytes(self):
    mailbox = ImapMailbox.from_bytes(b'(\\HasNoChildren \\Marked) "/" "INBOX"')

    assert mailbox.__class__ is ImapMailbox

    assert mailbox.name == "INBOX"
    assert mailbox.location == ""
    assert mailbox.delimiter == "/"

    assert not mailbox.has_children

    assert mailbox.is_marked
    assert mailbox.is_selectable

    assert not mailbox.is_draft
    assert not mailbox.is_sent
    assert not mailbox.is_spam
    assert not mailbox.is_trash

  def test_from_bytes_connector(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "INBOX"')

    assert mailbox.__class__ is ImapMailbox
    assert mailbox.connector == self.connector


  def test_from_bytes_subfolder(self):
    mailbox = ImapMailbox.from_bytes(b'(\\HasNoChildren \\Sent) "/" "MyFolder/MySubFolder/MyTestFolder"')

    assert mailbox.__class__ is ImapMailbox

    assert mailbox.name == "MyTestFolder"
    assert mailbox.location == "MyFolder/MySubFolder"
    assert mailbox.delimiter == "/"

    assert not mailbox.has_children

    assert not mailbox.is_marked
    assert mailbox.is_selectable

    assert not mailbox.is_draft
    assert mailbox.is_sent
    assert not mailbox.is_spam
    assert not mailbox.is_trash

  def test_from_bytes_exotic_delimiter(self):
    mailbox = ImapMailbox.from_bytes(b'(\\HasNoChildren \\Noselect \\Trash) "@" "MyFolder@MySubFolder@MyTestFolder"')

    assert mailbox.__class__ is ImapMailbox

    assert mailbox.name == "MyTestFolder"
    assert mailbox.location == "MyFolder@MySubFolder"
    assert mailbox.delimiter == "@"

    assert not mailbox.has_children

    assert not mailbox.is_marked
    assert not mailbox.is_selectable

    assert not mailbox.is_draft
    assert not mailbox.is_sent
    assert not mailbox.is_spam
    assert mailbox.is_trash

  def test_list_mailbox_without_connector(self):
    mailbox = ImapMailbox.from_bytes(b'(\\HasNoChildren \\Marked) "/" "INBOX"')

    with pytest.raises(ImapMailboxWithoutConnector):
        mailbox.list_mailbox()


  def test_list_mailbox(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailboxes = mailbox.list_mailbox()

    assert len(mailboxes) > 0

    assert mailboxes[0].name == "GitHub"
    assert mailboxes[0].location == ""

    assert mailboxes[1].name == "CI"
    assert mailboxes[1].location == "GitHub"

    assert mailboxes[2].name == "Actions"
    assert mailboxes[2].location == "GitHub/CI"

  def test_list_mailbox_from_mailbox(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailboxes = mailbox.list_mailbox()

    mailboxes = mailboxes[1].list_mailbox()

    assert len(mailboxes) > 0

    assert mailboxes[0].name == "CI"
    assert mailboxes[0].location == "GitHub"

    assert mailboxes[1].name == "Actions"
    assert mailboxes[1].location == "GitHub/CI"