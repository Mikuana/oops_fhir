from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TelecommunicationCapabilities"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TelecommunicationCapabilities:
    """
    v3 Code System TelecommunicationCapabilities

      Description:  Concepts that define the telecommunication capabilities
of a particular device. Used to identify the expected capabilities to be
found at a particular telecommunication address.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TelecommunicationCapabilities
    """

    data = CodeSystemConcept(
        {
            "code": "data",
            "definition": "Description: This device can receive data calls (i.e. modem).",
            "display": "data",
        }
    )
    """
    data

    Description: This device can receive data calls (i.e. modem).
    """

    fax = CodeSystemConcept(
        {
            "code": "fax",
            "definition": "Description: This device can receive faxes.",
            "display": "fax",
        }
    )
    """
    fax

    Description: This device can receive faxes.
    """

    sms = CodeSystemConcept(
        {
            "code": "sms",
            "definition": "Description: This device can receive SMS messages.",
            "display": "sms",
        }
    )
    """
    sms

    Description: This device can receive SMS messages.
    """

    tty = CodeSystemConcept(
        {
            "code": "tty",
            "definition": "Description: This device is a text telephone.",
            "display": "text",
        }
    )
    """
    text

    Description: This device is a text telephone.
    """

    voice = CodeSystemConcept(
        {
            "code": "voice",
            "definition": "Description: This device can receive voice calls (i.e. talking to another person, or a recording device, or a voice activated computer).",
            "display": "voice",
        }
    )
    """
    voice

    Description: This device can receive voice calls (i.e. talking to another person, or a recording device, or a voice activated computer).
    """

    class Meta:
        resource = _resource
