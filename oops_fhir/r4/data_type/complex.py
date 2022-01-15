from typing import Optional

from oops_fhir.r4.data_type import primitive as p
from oops_fhir.r4.value_set import mime_types
from oops_fhir.r4.value_set import common_languages

class Attachment:
    content_type: Optional[p.code] = None
    """ Mime type of the content, with charset etc. """
    language: Optional[p.code] = common_languages.en_us
    """ Human language of the content (BCP-47) """
    data: Optional[p.base_64_binary] = None
    """ Data inline, base64ed """
    url: Optional[p.url] = None
    """ Uri where the data can be found """
    size: Optional[p.unsigned_int] = None
    """ Number of bytes of content (if url provided) """
    hash: Optional[p.base_64_binary] = None
    """ Hash of the data (sha-1, base64ed) """
    title: Optional[p.string] = None
    """ Label to display in place of the data """
    creation: Optional[p.datetime] = None
    """ date attachment was first created """



Attachment.language
