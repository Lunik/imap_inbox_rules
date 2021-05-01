# IMAP inbox Rules

[![codecov](https://codecov.io/gh/Lunik/imap_inbox_rules/branch/master/graph/badge.svg?token=1OBCJMJ3IY)](https://codecov.io/gh/Lunik/imap_inbox_rules)

Python tools to organize IMAP inbox

## Usage

### Initiate connector

```python
from imapinboxrules.connector import ConnectorFactory

connector = ConnectorFactory.get_connector('imap')(host="imap.gmail.com")

connector.login(
  user="my.username@gmail.com",
  password="my_secret_password")
```

### List mailboxes

List all mailboxes from root :
```python
mailboxes = connector.list_mailbox()

for mailbox in mailboxes:
  print(mailbox.name)
```

List sub-mailboxes :
```python
mailboxes = connector.list_mailbox()[1].list_mailbox()

for mailbox in mailboxes:
  print(mailbox.name)
```

For advanced usage read [imaplib documentation on `list` method](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.list)

## Coverage

[![codecov](https://codecov.io/gh/Lunik/imap_inbox_rules/branch/master/graphs/tree.svg?token=1OBCJMJ3IY)

## Built with

[Python imaplib](https://docs.python.org/3/library/imaplib.html)
