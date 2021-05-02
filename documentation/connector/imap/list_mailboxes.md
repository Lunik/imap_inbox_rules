# List mailboxes with IMAP connector

## Requirements

- [Init IMAP Connector](init.md)

## Usage

List all mailboxes from root :
```python
mailboxes = connector.list_mailbox()

for mailbox in mailboxes:
  print(mailbox.name)
```

For advanced usage read [imaplib documentation on `list` method](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.list)
