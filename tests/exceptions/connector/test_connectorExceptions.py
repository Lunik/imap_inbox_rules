import pytest

from imapinboxrules.exceptions.connector import *

class TestClassConnectorExceptions:

  def test_ConnectorError(self):
    exception = ConnectorError("Some error")

    with pytest.raises(ConnectorError):
      raise exception

  def test_ConnectorNotFound(self):
    exception = ConnectorNotFound("Some connector")

    with pytest.raises(ConnectorNotFound):
      raise exception

  def test_ObjectWithoutConnector(self):
    exception = ObjectWithoutConnector()

    with pytest.raises(ObjectWithoutConnector):
      raise exception
