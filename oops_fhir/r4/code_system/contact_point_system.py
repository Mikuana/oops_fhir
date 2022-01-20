from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ContactPointSystem"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ContactPointSystem:
    """
    ContactPointSystem

    Telecommunications form for contact point.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/contact-point-system
    """

    phone = CodeSystemConcept(
        {
            "code": "phone",
            "definition": "The value is a telephone number used for voice calls. Use of full international numbers starting with + is recommended to enable automatic dialing support but not required.",
            "display": "Phone",
        }
    )
    """
    Phone

    The value is a telephone number used for voice calls. Use of full international numbers starting with + is recommended to enable automatic dialing support but not required.
    """

    fax = CodeSystemConcept(
        {
            "code": "fax",
            "definition": "The value is a fax machine. Use of full international numbers starting with + is recommended to enable automatic dialing support but not required.",
            "display": "Fax",
        }
    )
    """
    Fax

    The value is a fax machine. Use of full international numbers starting with + is recommended to enable automatic dialing support but not required.
    """

    email = CodeSystemConcept(
        {
            "code": "email",
            "definition": "The value is an email address.",
            "display": "Email",
        }
    )
    """
    Email

    The value is an email address.
    """

    pager = CodeSystemConcept(
        {
            "code": "pager",
            "definition": "The value is a pager number. These may be local pager numbers that are only usable on a particular pager system.",
            "display": "Pager",
        }
    )
    """
    Pager

    The value is a pager number. These may be local pager numbers that are only usable on a particular pager system.
    """

    url = CodeSystemConcept(
        {
            "code": "url",
            "definition": "A contact that is not a phone, fax, pager or email address and is expressed as a URL.  This is intended for various institutional or personal contacts including web sites, blogs, Skype, Twitter, Facebook, etc. Do not use for email addresses.",
            "display": "URL",
        }
    )
    """
    URL

    A contact that is not a phone, fax, pager or email address and is expressed as a URL.  This is intended for various institutional or personal contacts including web sites, blogs, Skype, Twitter, Facebook, etc. Do not use for email addresses.
    """

    sms = CodeSystemConcept(
        {
            "code": "sms",
            "definition": "A contact that can be used for sending an sms message (e.g. mobile phones, some landlines).",
            "display": "SMS",
        }
    )
    """
    SMS

    A contact that can be used for sending an sms message (e.g. mobile phones, some landlines).
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": 'A contact that is not a phone, fax, page or email address and is not expressible as a URL.  E.g. Internal mail address.  This SHOULD NOT be used for contacts that are expressible as a URL (e.g. Skype, Twitter, Facebook, etc.)  Extensions may be used to distinguish "other" contact types.',
            "display": "Other",
        }
    )
    """
    Other

    A contact that is not a phone, fax, page or email address and is not expressible as a URL.  E.g. Internal mail address.  This SHOULD NOT be used for contacts that are expressible as a URL (e.g. Skype, Twitter, Facebook, etc.)  Extensions may be used to distinguish "other" contact types.
    """

    class Meta:
        resource = _resource
