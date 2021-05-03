
class MailboxNotFound(Exception):

  def __init__(self, mailbox_name):
    super().__init__("Mailbox with name '{}' not found.".format(mailbox_name))

class MailboxCheckFailed(Exception):

  def __init__(self, mailbox_name, error):
    super().__init__("Mailbox with name '{}' fail check with error : {}".format(mailbox_name, error))