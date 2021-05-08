
from .mail_filter import MailFilter

class MailFilterContainsInFrom(MailFilter):

  def __init__(self, *words):
    self.words = words

  def match(self, mail):
    mail_from = mail.headers('From')

    for word in words:
      if word in mail_from:
        return True

    return False