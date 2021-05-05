import pytest

from imapinboxrules.model.imap.ImapMailboxAttributes import ImapMailboxAttributes

class TestClassImapMailboxAttributes:

  
  def test_has_children(self):

    assert ImapMailboxAttributes.has_children("\\HasChildren")
    assert ImapMailboxAttributes.has_children("\\Unmarked \\HasChildren")

    assert not ImapMailboxAttributes.has_children("\\HasNoChildren")
    assert not ImapMailboxAttributes.has_children("\\Marked \\HasNoChildren \\Trash")

    assert ImapMailboxAttributes.has_children("\\HasChildren \\HasNoChildren")

    assert not ImapMailboxAttributes.has_children("")

  
  def test_has_not_children(self):

    assert ImapMailboxAttributes.has_not_children("\\HasNoChildren")
    assert ImapMailboxAttributes.has_not_children("\\Marked \\HasNoChildren \\Trash")

    assert not ImapMailboxAttributes.has_not_children("\\HasChildren")
    assert not ImapMailboxAttributes.has_not_children("\\Unmarked \\HasChildren")

    assert ImapMailboxAttributes.has_not_children("\\HasChildren \\HasNoChildren")

    assert not ImapMailboxAttributes.has_not_children("")

    assert ImapMailboxAttributes.has_not_children("\\Noinferiors")

  
  def test_is_marked(self):

    assert ImapMailboxAttributes.is_marked("\\Marked")
    assert ImapMailboxAttributes.is_marked("\\Marked \\HasChildren")
    assert ImapMailboxAttributes.is_marked("\\HasChildren \\Marked \\Trash")

    assert not ImapMailboxAttributes.is_marked("\\Unmarked")
    assert not ImapMailboxAttributes.is_marked("\\Unmarked")

    assert not ImapMailboxAttributes.is_marked("")

  
  def test_is_not_marked(self):

    assert ImapMailboxAttributes.is_not_marked("\\Unmarked")
    assert ImapMailboxAttributes.is_not_marked("\\Unmarked \\HasChildren")
    assert ImapMailboxAttributes.is_not_marked("\\HasChildren \\Unmarked \\Trash")

    assert not ImapMailboxAttributes.is_not_marked("\\marked")
    assert not ImapMailboxAttributes.is_not_marked("\\marked")

    assert not ImapMailboxAttributes.is_not_marked("")

  
  def test_is_not_selectable(self):
    assert ImapMailboxAttributes.is_not_selectable("\\Noselect")
    assert ImapMailboxAttributes.is_not_selectable("\\Noselect \\HasChildren")
    assert ImapMailboxAttributes.is_not_selectable("\\HasChildren \\Noselect \\Trash")

    assert not ImapMailboxAttributes.is_not_selectable("")
    assert not ImapMailboxAttributes.is_not_selectable("\\HasChildren")

  
  def test_is_selectable(self):
    assert ImapMailboxAttributes.is_selectable("")
    assert ImapMailboxAttributes.is_selectable("\\HasChildren")
    assert ImapMailboxAttributes.is_selectable("\\HasChildren \\Trash")

    assert not ImapMailboxAttributes.is_selectable("\\Noselect")
    assert not ImapMailboxAttributes.is_selectable("\\HasChildren \\Noselect")

  
  def test_is_sent(self):
    assert ImapMailboxAttributes.is_sent("\\Sent")
    assert ImapMailboxAttributes.is_sent("\\Sent \\HasChildren")
    assert ImapMailboxAttributes.is_sent("\\HasChildren \\Sent \\Trash")

    assert not ImapMailboxAttributes.is_sent("")
    assert not ImapMailboxAttributes.is_sent("\\HasChildren")

  
  def test_is_spam(self):
    assert ImapMailboxAttributes.is_spam("\\Spam")
    assert ImapMailboxAttributes.is_spam("\\Spam \\HasChildren")
    assert ImapMailboxAttributes.is_spam("\\HasChildren \\Spam \\Trash")

    assert ImapMailboxAttributes.is_spam("\\Junk")
    assert ImapMailboxAttributes.is_spam("\\Junk \\HasChildren")
    assert ImapMailboxAttributes.is_spam("\\HasChildren \\Junk \\Trash")

    assert ImapMailboxAttributes.is_spam("\\Spam \\Junk")

    assert not ImapMailboxAttributes.is_spam("")
    assert not ImapMailboxAttributes.is_spam("\\HasChildren")

  
  def test_is_draft(self):
    assert ImapMailboxAttributes.is_draft("\\Drafts")
    assert ImapMailboxAttributes.is_draft("\\Drafts \\HasChildren")
    assert ImapMailboxAttributes.is_draft("\\HasChildren \\Draft \\Trash")

    assert ImapMailboxAttributes.is_draft("\\Drafts")
    assert ImapMailboxAttributes.is_draft("\\Drafts \\HasChildren")
    assert ImapMailboxAttributes.is_draft("\\HasChildren \\Draft \\Trash")

    assert ImapMailboxAttributes.is_draft("\\Drafts \\Draft")

    assert not ImapMailboxAttributes.is_draft("")
    assert not ImapMailboxAttributes.is_draft("\\HasChildren")

  
  def test_is_trash(self):
    assert ImapMailboxAttributes.is_trash("\\Trash")
    assert ImapMailboxAttributes.is_trash("\\Trash \\HasChildren")
    assert ImapMailboxAttributes.is_trash("\\HasChildren \\Trash \\Sent")

    assert not ImapMailboxAttributes.is_trash("")
    assert not ImapMailboxAttributes.is_trash("\\HasChildren")