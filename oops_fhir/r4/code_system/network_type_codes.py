from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["NetworkTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class NetworkTypeCodes:
    """
    Network Type Codes

    This value set includes a smattering of Network type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/benefit-network
    """

    in_ = CodeSystemConcept(
        {
            "code": "in",
            "definition": "Services rendered by a Network provider",
            "display": "In Network",
        }
    )
    """
    In Network

    Services rendered by a Network provider
    """

    out = CodeSystemConcept(
        {
            "code": "out",
            "definition": "Services rendered by a provider who is not in the Network",
            "display": "Out of Network",
        }
    )
    """
    Out of Network

    Services rendered by a provider who is not in the Network
    """

    class Meta:
        resource = _resource
