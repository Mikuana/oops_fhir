from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ContainerSeparator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ContainerSeparator:
    """
    v3 Code System ContainerSeparator

     A material in a blood collection container that facilites the
separation of of blood cells from serum or plasma

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ContainerSeparator
    """

    gel = CodeSystemConcept(
        {
            "code": "GEL",
            "definition": "A gelatinous type of separator material.",
            "display": "Gel",
        }
    )
    """
    Gel

    A gelatinous type of separator material.
    """

    none = CodeSystemConcept(
        {
            "code": "NONE",
            "definition": "No separator material is present in the container.",
            "display": "None",
        }
    )
    """
    None

    No separator material is present in the container.
    """

    class Meta:
        resource = _resource
