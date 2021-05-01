from imapinboxrules.exceptions.connector import ConnectorNotFound

from .imap import ImapConnector

class ConnectorFactory:

  connectors = {
    'imap': ImapConnector
  }

  @classmethod
  def get_connector(cls, name):
    if name not in cls.connectors:
      raise ConnectorNotFound(name)

    return cls.connectors[name]
