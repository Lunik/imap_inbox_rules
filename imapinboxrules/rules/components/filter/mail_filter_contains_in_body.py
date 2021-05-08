
from .mail_filter import MailFilter

class MailFilterContainsInBody(MailFilter):

  def __init__(self, body_type, *words):
    self.words = words
    self.body_type = body_type

  def match(self, mail):
    mail_body = mail.body(self.body_type)

    for word in words:
      if word in mail_body:
        return True

    return False