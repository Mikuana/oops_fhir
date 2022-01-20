from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["UDICodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class UDICodes:
    """
    UDI Codes

    This value set includes sample UDI codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-udi
    """

    gudid = CodeSystemConcept(
        {
            "code": "gudid",
            "definition": "GUDID (FDA) US Repository",
            "display": "GUDID (FDA)",
        }
    )
    """
    GUDID (FDA)

    GUDID (FDA) US Repository
    """

    class Meta:
        resource = _resource
