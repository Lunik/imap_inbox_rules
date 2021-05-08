
class MailAction:
  @abstractmethod
  def apply(self, connector, mail):
      pass