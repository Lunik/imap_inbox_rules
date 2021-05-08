
from .mail_filter import MailFilter

class MailFilterFrom(MailFilter):

  def __init__(self, *email_adresses):
    self.email_adresses = email_adresses

  def match(self, mail):
    mail_from = mail.headers('From')

    return mail_from in self.email_adresses