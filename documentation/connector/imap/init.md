# Init IMAP connector

## Requirements

- A valid IMAP account

## Usage

```python
from imapinboxrules.connector import ConnectorFactory

connector = ConnectorFactory.get_connector('imap')(host="imap.gmail.com")

connector.login(
  user="my.username@gmail.com",
  password="my_secret_password")
```