from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["verificationresultcommunicationmethod"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class verificationresultcommunicationmethod:
    """
    VerificationResult Communication Method

    Attested information may be validated by process that are manual or
automated. For automated processes it may accomplished by the system of
record reaching out through another system's API or information may be
sent to the system of record. This value set defines a set of codes to
describing the process, the how, a resource or data element is
validated.

    Status: active - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/verificationresult-communication-method
    """

    manual = CodeSystemConcept(
        {
            "code": "manual",
            "definition": "The information is submitted/retrieved manually (e.g. by phone, fax, paper-based)",
            "display": "Manual",
        }
    )
    """
    Manual

    The information is submitted/retrieved manually (e.g. by phone, fax, paper-based)
    """

    portal = CodeSystemConcept(
        {
            "code": "portal",
            "definition": "The information is submitted/retrieved via a portal",
            "display": "Portal",
        }
    )
    """
    Portal

    The information is submitted/retrieved via a portal
    """

    pull = CodeSystemConcept(
        {
            "code": "pull",
            "definition": "The information is retrieved (i.e. pulled) from a source (e.g. over an API)",
            "display": "Pull",
        }
    )
    """
    Pull

    The information is retrieved (i.e. pulled) from a source (e.g. over an API)
    """

    push = CodeSystemConcept(
        {
            "code": "push",
            "definition": "The information is sent (i.e. pushed) from a source (e.g. over an API, asynchronously, secure messaging)",
            "display": "Push",
        }
    )
    """
    Push

    The information is sent (i.e. pushed) from a source (e.g. over an API, asynchronously, secure messaging)
    """

    class Meta:
        resource = _resource
