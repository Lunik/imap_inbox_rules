
from .mail_filter import MailFilter

class MailFilterContainsInSubject(MailFilter):

  def __init__(self, *words):
    self.words = words

  def match(self, mail):
    mail_subject = mail.headers('Subject')

    for word in words:
      if word in mail_subject:
        return True

    return False