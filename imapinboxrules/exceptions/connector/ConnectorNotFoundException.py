
class ConnectorNotFoundException(Exception):

  def __init__(self, connector_name):
    super().__init__("Connector with name '{}' not found.".format(connector_name))