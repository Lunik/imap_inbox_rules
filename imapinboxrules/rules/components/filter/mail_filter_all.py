
from .mail_filter import MailFilter

class MailFilterAll(MailFilter):

  def __init__(self):

  def match(self, mail):
    return True