
class ImapMailNotFound(Exception):

  def __init__(self, id):
    super().__init__("Mail with id(s) '{}' not found.".format(id))

class ImapMailNotLoaded(Exception):

  def __init__(self, id):
    super().__init__("Mail not loaded.")