
from .mail_filter import MailFilter
from .mail_filter_contains_in_subject import MailFilterContainsInSubject
from .mail_filter_contains_in_body import MailFilterContainsInBody

class MailFilterContainsInSubjectOrBody(MailFilter):

  def __init__(self, body_type, *words):
    self.words = words
    self.body_type = body_type

    self.filter_in_subject = MailFilterContainsInSubject(*words)
    self.filter_in_body = MailFilterContainsInBody(body_type, *words)

  def match(self, mail):
    return self.filter_in_subject.match(mail) or self.filter_in_body.match(mail)