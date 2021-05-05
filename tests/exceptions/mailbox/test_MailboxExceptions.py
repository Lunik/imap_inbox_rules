import pytest

from imapinboxrules.exceptions.mailbox import *

class TestClassMailboxExceptions:

  def test_MailboxNotFound(self):
    exception = MailboxNotFound("MAILBOX")

    with pytest.raises(MailboxNotFound):
      raise exception

  def test_MailboxCheckFailed(self):
    exception = MailboxCheckFailed("MAILBOX", "some error")

    with pytest.raises(MailboxCheckFailed):
      raise exception
