from imapinboxrules.exceptions.connector import ObjectWithoutConnector

def require_connector(func):
  def inner(self, *args, **kwargs):
    if self.connector is None:
      raise ObjectWithoutConnector()

    return func(self, *args, **kwargs)

  return inner