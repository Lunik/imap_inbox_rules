import pytest

from imapinboxrules.exceptions.model.imap import *

class TestClassImapExceptions:

  def test_imap_mail_not_found(self):
    with pytest.raises(ImapMailNotFound):
      raise ImapMailNotFound("99")

  def test_imap_mail_not_loaded(self):
    with pytest.raises(ImapMailNotLoaded):
      raise ImapMailNotLoaded("99")
