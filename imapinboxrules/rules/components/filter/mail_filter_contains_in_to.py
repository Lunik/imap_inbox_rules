
from .mail_filter import MailFilter

class MailFilterContainsInTo(MailFilter):

  def __init__(self, *words):
    self.words = words

  def match(self, mail):
    mail_to = mail.headers('To')

    for word in words:
      if word in mail_to:
        return True

    return False