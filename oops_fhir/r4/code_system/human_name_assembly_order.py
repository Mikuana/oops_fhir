from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["HumanNameAssemblyOrder"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class HumanNameAssemblyOrder:
    """
    HumanNameAssemblyOrder

    A code that represents the preferred display order of the components of
a human name.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/name-assembly-order
    """

    nl1 = CodeSystemConcept({"code": "NL1", "display": "Own Name"})
    """
    Own Name

    
    """

    nl2 = CodeSystemConcept({"code": "NL2", "display": "Partner Name"})
    """
    Partner Name

    
    """

    nl3 = CodeSystemConcept(
        {"code": "NL3", "display": "Partner Name followed by Maiden Name"}
    )
    """
    Partner Name followed by Maiden Name

    
    """

    nl4 = CodeSystemConcept(
        {"code": "NL4", "display": "Own Name followed by Partner Name"}
    )
    """
    Own Name followed by Partner Name

    
    """

    class Meta:
        resource = _resource
