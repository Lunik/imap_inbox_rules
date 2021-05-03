import pytest

from imapinboxrules.exceptions.model.imap import *

class TestClassImapExceptions:

  def test_ImapMailNotFound(self):
    exception = ImapMailNotFound("99")

    with pytest.raises(ImapMailNotFound):
      raise exception

  def test_ImapMailNotLoaded(self):
    exception = ImapMailNotLoaded("99")

    with pytest.raises(ImapMailNotLoaded):
      raise exception
