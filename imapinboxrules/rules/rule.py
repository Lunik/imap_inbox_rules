
class MailboxRule:
  def __init__(self, name, filters=[], actions=[], exclusions=[], final=False):
    self.name = name
    self.filters = filters
    self.actions = actions
    self.exclusions = exclusions
    self.final = final

  def handle(self, mail, dry_run=False):

    if not mail.loaded:
      mail.load()

    match_count = 0
    for filter_obj in self.filters:
      match_count += filter_obj.match(email)

    for exclusion in self.exclusions:
      match_count -= exclusion.match(email)

    if match_count == len(self.filters):
      print("[Rule][{}] Found matching mail".format(self.name))

      for action in self.actions:
        action.apply(mail, dry_run)
