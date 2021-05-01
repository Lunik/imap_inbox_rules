from imapinboxrules.exceptions.connector import ConnectorNotFoundException

from .imap import ImapConnector

class ConnectorFactory:

  connectors = {
    'imap': ImapConnector
  }

  @classmethod
  def get_connector(cls, name):
    if name not in cls.connectors:
      raise ConnectorNotFoundException(name)

    return cls.connectors[name]
