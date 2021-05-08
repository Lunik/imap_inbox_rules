
class MailFilter:
  @abstractmethod
  def match(self, mail):
      pass