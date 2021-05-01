import pytest

from imapinboxrules.connector import ConnectorFactory
from imapinboxrules.connector.imap import ImapConnector
from imapinboxrules.exceptions.connector import ConnectorNotFoundException

class TestClassConnectorFactory:

  def test_get_valid_connector(self):
    connector = ConnectorFactory.get_connector('imap')

    assert connector is ImapConnector


  def test_get_invalid_connector(self):
    with pytest.raises(ConnectorNotFoundException):
      connector = ConnectorFactory.get_connector('invalid')