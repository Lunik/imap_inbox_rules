# List sub-mailboxes from Mailbox

## Requirements

- [A Mailbox objectt](../imap/list_mailboxes.md)

## Usage

List sub-mailboxes :
```python
sub_mailboxes = mailbox.list_mailbox()

for sub_mailbox in sub_mailboxes:
  print(sub_mailbox.name)
```

For advanced usage read [imaplib documentation on `list` method](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.list)
