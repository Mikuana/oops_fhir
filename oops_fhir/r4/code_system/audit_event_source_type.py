from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventSourceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventSourceType:
    """
    Audit Event Source Type

    The type of process where the audit event originated from.

    Status: active - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/security-source-type
    """

    one = CodeSystemConcept(
        {
            "code": "1",
            "definition": "End-user display device, diagnostic device.",
            "display": "User Device",
        }
    )
    """
    User Device

    End-user display device, diagnostic device.
    """

    two = CodeSystemConcept(
        {
            "code": "2",
            "definition": "Data acquisition device or instrument.",
            "display": "Data Interface",
        }
    )
    """
    Data Interface

    Data acquisition device or instrument.
    """

    three = CodeSystemConcept(
        {
            "code": "3",
            "definition": "Web Server process or thread.",
            "display": "Web Server",
        }
    )
    """
    Web Server

    Web Server process or thread.
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "Application Server process or thread.",
            "display": "Application Server",
        }
    )
    """
    Application Server

    Application Server process or thread.
    """

    five = CodeSystemConcept(
        {
            "code": "5",
            "definition": "Database Server process or thread.",
            "display": "Database Server",
        }
    )
    """
    Database Server

    Database Server process or thread.
    """

    six = CodeSystemConcept(
        {
            "code": "6",
            "definition": "Security server, e.g. a domain controller.",
            "display": "Security Server",
        }
    )
    """
    Security Server

    Security server, e.g. a domain controller.
    """

    seven = CodeSystemConcept(
        {
            "code": "7",
            "definition": "ISO level 1-3 network component.",
            "display": "Network Device",
        }
    )
    """
    Network Device

    ISO level 1-3 network component.
    """

    eight = CodeSystemConcept(
        {
            "code": "8",
            "definition": "ISO level 4-6 operating software.",
            "display": "Network Router",
        }
    )
    """
    Network Router

    ISO level 4-6 operating software.
    """

    nine = CodeSystemConcept(
        {
            "code": "9",
            "definition": "Other kind of device (defined by DICOM, but some other code/system can be used).",
            "display": "Other",
        }
    )
    """
    Other

    Other kind of device (defined by DICOM, but some other code/system can be used).
    """

    class Meta:
        resource = _resource
