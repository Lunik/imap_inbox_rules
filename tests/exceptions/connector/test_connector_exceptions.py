import pytest

from imapinboxrules.exceptions.connector import *

class TestClassConnectorExceptions:

  def test_connector_error(self):
    with pytest.raises(ConnectorError):
      raise ConnectorError("Some error")

  def test_connector_not_found(self):
    with pytest.raises(ConnectorNotFound):
      raise ConnectorNotFound("Some connector")

  def test_object_without_connector(self):
    with pytest.raises(ObjectWithoutConnector):
      raise ObjectWithoutConnector()
