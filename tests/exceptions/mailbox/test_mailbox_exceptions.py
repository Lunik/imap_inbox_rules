import pytest

from imapinboxrules.exceptions.mailbox import *

class TestClassMailboxExceptions:

  def test_mailbox_not_found(self):
    with pytest.raises(MailboxNotFound):
      raise MailboxNotFound("MAILBOX")

  def test_mailbox_check_failed(self):
    with pytest.raises(MailboxCheckFailed):
      raise MailboxCheckFailed("MAILBOX", "some error")
