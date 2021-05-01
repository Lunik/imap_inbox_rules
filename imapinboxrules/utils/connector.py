from imapinboxrules.exceptions.model.imap import ImapMailboxWithoutConnector

def require_connector(func):
  def inner(self, *args, **kwargs):
    if self.connector is None:
      raise ImapMailboxWithoutConnector()

    return func(self, *args, **kwargs)

  return inner