
class ImapMailboxWithoutConnector(Exception):

  def __init__(self):
    super().__init__("ImapMailbox was not initiated with connector.")