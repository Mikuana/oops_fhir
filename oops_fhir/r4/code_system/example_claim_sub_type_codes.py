from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleClaimSubTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleClaimSubTypeCodes:
    """
    Example Claim SubType Codes

    This value set includes sample Claim SubType codes which are used to
distinguish the claim types for example within type institutional there
may be subtypes for emergency services, bed stay and transportation.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/ex-claimsubtype
    """

    ortho = CodeSystemConcept(
        {
            "code": "ortho",
            "definition": "A claim for Orthodontic Services.",
            "display": "Orthodontic Claim",
        }
    )
    """
    Orthodontic Claim

    A claim for Orthodontic Services.
    """

    emergency = CodeSystemConcept(
        {
            "code": "emergency",
            "definition": "A claim for emergency services.",
            "display": "Emergency Claim",
        }
    )
    """
    Emergency Claim

    A claim for emergency services.
    """

    class Meta:
        resource = _resource
