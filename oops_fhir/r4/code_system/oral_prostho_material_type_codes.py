from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["OralProsthoMaterialTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class OralProsthoMaterialTypeCodes:
    """
    Oral Prostho Material type Codes

    This value set includes sample Oral Prosthodontic Material type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-oralprostho
    """

    one = CodeSystemConcept(
        {"code": "1", "definition": "Fixed Bridge", "display": "Fixed Bridge"}
    )
    """
    Fixed Bridge

    Fixed Bridge
    """

    two = CodeSystemConcept(
        {"code": "2", "definition": "Maryland Bridge", "display": "Maryland Bridge"}
    )
    """
    Maryland Bridge

    Maryland Bridge
    """

    three = CodeSystemConcept(
        {"code": "3", "definition": "Denture Acrylic", "display": "Denture Acrylic"}
    )
    """
    Denture Acrylic

    Denture Acrylic
    """

    four = CodeSystemConcept(
        {
            "code": "4",
            "definition": "Denture Chrome Cobalt",
            "display": "Denture Chrome Cobalt",
        }
    )
    """
    Denture Chrome Cobalt

    Denture Chrome Cobalt
    """

    class Meta:
        resource = _resource
