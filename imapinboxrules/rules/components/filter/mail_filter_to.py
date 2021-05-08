
from .mail_filter import MailFilter

class MailFilterTo(MailFilter):

  def __init__(self, *email_adresses):
    self.email_adresses = email_adresses

  def match(self, mail):
    mail_from = mail.headers('To')

    return mail_from in self.email_adresses