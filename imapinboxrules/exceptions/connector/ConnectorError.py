
class ConnectorError(Exception):

  def __init__(self, err):
    super().__init__("Connector Error : {}".format(err))