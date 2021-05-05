import pytest
import os

from dotenv import load_dotenv

from imapinboxrules.model.imap import ImapMailbox
from imapinboxrules.connector import ConnectorFactory
from imapinboxrules.exceptions.connector import ObjectWithoutConnector

class TestClassImapMailbox:

  def setup_method(self, method):
    load_dotenv()

    connector = ConnectorFactory.get_connector('imap')

    self.connector = connector(ssl=False, host=os.environ.get('TEST_IMAP_HOST'), port=os.environ.get('TEST_IMAP_PORT'))

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

    with pytest.raises(ObjectWithoutConnector):
        mailbox.list_mailbox()


  def test_list_mailbox(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailboxes = mailbox.list_mailbox()

    assert len(mailboxes) > 0

    assert mailboxes[0].name == "CI"
    assert mailboxes[0].location == "GitHub"

    assert mailboxes[1].name == "Actions"
    assert mailboxes[1].location == "GitHub.CI"

  def test_list_mailbox_from_mailbox(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailboxes = mailbox.list_mailbox()

    mailboxes = mailboxes[0].list_mailbox()

    assert len(mailboxes) > 0

    assert mailboxes[0].name == "Actions"
    assert mailboxes[0].location == "GitHub.CI"

  def test_select_mailbox(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailbox.select()

  def test_count_mail(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailbox.select()

    assert mailbox.count_mail == 3

  def test_search_mail(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailbox.select()

    mails = mailbox.search_mail(charset=None, criterion=["(FROM \"noreply@github.com\")"])

    assert len(mails) == 1

  def test_search_mail_unkown(self):
    mailbox = ImapMailbox.from_bytes_with_connector(self.connector, b'(\\HasNoChildren \\Marked) "/" "GitHub"')

    mailbox.select()

    mails = mailbox.search_mail(charset=None, criterion=["(FROM \"unknown@invalid.local\")"])

    assert len(mails) == 0