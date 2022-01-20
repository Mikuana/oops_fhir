from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["need"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class need:
    """
    Need

    The frequency with which the target must be validated

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/need
    """

    none = CodeSystemConcept(
        {"code": "none", "definition": "***TODO***", "display": "None"}
    )
    """
    None

    ***TODO***
    """

    initial = CodeSystemConcept(
        {"code": "initial", "definition": "***TODO***", "display": "Initial"}
    )
    """
    Initial

    ***TODO***
    """

    periodic = CodeSystemConcept(
        {"code": "periodic", "definition": "***TODO***", "display": "Periodic"}
    )
    """
    Periodic

    ***TODO***
    """

    class Meta:
        resource = _resource
