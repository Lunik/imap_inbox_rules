import re
import email
import base64
import quopri

from imapinboxrules.utils.connector import require_connector
from imapinboxrules.exceptions.model.imap import ImapMailNotLoaded

class ImapMail:

  connector = None

  id = -1

  email = None

  @staticmethod
  def from_id(id):

    imap_mail = ImapMail()
    imap_mail.id = int(id)

    return imap_mail

  @staticmethod
  def from_id_with_connector(connector, id):
    mail = ImapMail.from_id(id)

    mail.connector = connector

    return mail

  @require_connector
  def load(self):
    self.email = email.message_from_bytes(self.connector.fetch_mail(str(self.id), '(RFC822)'))

  def header(self, header):
    if self.email is None:
      raise ImapMailNotLoaded(self.id)

    return email.header.make_header(email.header.decode_header(self.email[header]))

  @staticmethod
  def _decode_playload(enc, data):
    if enc == "base64":
      return base64.b64decode(data)
    elif enc == "quoted-printable":
      return quopri.decodestring(data)

    return b""

  @staticmethod
  def __parse_body(emailobj, type="text/plain"):

    def _get_body(emailobj):

      content = []
      if emailobj.is_multipart():
        for payload in emailobj.get_payload():
          if payload.is_multipart():
              content.append(_get_body(payload))

          body = payload.get_payload()
          charset = payload.get_charset()
          if charset is None:
            charset = "UTF-8"

          if payload.get_content_type() == type:
            print(ImapMail._decode_playload(payload["Content-Transfer-Encoding"], body))
            content.append(ImapMail._decode_playload(payload["Content-Transfer-Encoding"], body).decode(charset))
      else:
        return emailobj.get_payload()

      return "\n".join(content)

    return _get_body(emailobj) 

  def body(self, type="text/plain"):
    if self.email is None:
      raise ImapMailNotLoaded(self.id)

    return self.__parse_body(self.email, type)