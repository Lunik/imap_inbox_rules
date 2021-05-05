
class ImapMailboxAttributes:

  # rfc3501
  # https://tools.ietf.org/html/rfc3501#section-7.2.2

  children = ["\\HasChildren"]
  not_children = ["\\HasNoChildren", "\\Noinferiors"]

  marked = ["\\Marked"]
  not_marked = ["\\Unmarked"]
  not_selectable = ["\\Noselect"]

  sent = ["\\Sent"]
  spam = ["\\Junk", "\\Spam"]
  draft = ["\\Drafts", "\\Draft"]
  trash = ["\\Trash"]

  @staticmethod
  def __check_attr(attrs, mailbox_attributes):
    for attr in attrs:
      if attr in mailbox_attributes:
        return True

    return False

  @staticmethod
  def has_children(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.children, mailbox_attributes)

  @staticmethod
  def has_not_children(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.not_children, mailbox_attributes)

  @staticmethod
  def is_marked(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.marked, mailbox_attributes)

  @staticmethod
  def is_not_marked(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.not_marked, mailbox_attributes)

  @staticmethod
  def is_not_selectable(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.not_selectable, mailbox_attributes)

  @staticmethod
  def is_selectable(mailbox_attributes):
    return not ImapMailboxAttributes.is_not_selectable(mailbox_attributes)

  @staticmethod
  def is_sent(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.sent, mailbox_attributes)

  @staticmethod
  def is_spam(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.spam, mailbox_attributes)

  @staticmethod
  def is_draft(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.draft, mailbox_attributes)

  @staticmethod
  def is_trash(mailbox_attributes):
    return ImapMailboxAttributes.__check_attr(ImapMailboxAttributes.trash, mailbox_attributes)