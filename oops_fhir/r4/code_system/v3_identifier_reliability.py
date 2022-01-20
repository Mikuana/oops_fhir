from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3IdentifierReliability"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3IdentifierReliability:
    """
    v3 Code System IdentifierReliability

     Specifies the reliability with which the identifier is known. This
attribute MAY be used to assist with identifier matching algorithms.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-IdentifierReliability
    """

    iss = CodeSystemConcept(
        {
            "code": "ISS",
            "definition": "Description: The identifier was issued by the system responsible for constructing the instance.",
            "display": "Issued by System",
        }
    )
    """
    Issued by System

    Description: The identifier was issued by the system responsible for constructing the instance.
    """

    unv = CodeSystemConcept(
        {
            "code": "UNV",
            "definition": "Description: The identifier was provided to the system that constructed the instance, but has not been verified. e.g. a Drivers  license entered manually into a system by a user.",
            "display": "Unverified by system",
        }
    )
    """
    Unverified by system

    Description: The identifier was provided to the system that constructed the instance, but has not been verified. e.g. a Drivers  license entered manually into a system by a user.
    """

    vrf = CodeSystemConcept(
        {
            "code": "VRF",
            "definition": "Description: The identifier was not issued by the system responsible for constructing the instance, but the system that captured the id has verified the identifier with the issuing authority, or with another system that has verified the identifier.",
            "display": "Verified by system",
        }
    )
    """
    Verified by system

    Description: The identifier was not issued by the system responsible for constructing the instance, but the system that captured the id has verified the identifier with the issuing authority, or with another system that has verified the identifier.
    """

    class Meta:
        resource = _resource
