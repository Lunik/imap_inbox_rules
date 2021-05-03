
class ConnectorError(Exception):

  def __init__(self, err):
    super().__init__("Connector Error : {}".format(err))


class ConnectorNotFound(Exception):

  def __init__(self, connector_name):
    super().__init__("Connector with name '{}' not found.".format(connector_name))

class ObjectWithoutConnector(Exception):

  def __init__(self):
    super().__init__("Object was not initiated with connector.")