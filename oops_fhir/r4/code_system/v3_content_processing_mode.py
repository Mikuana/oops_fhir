from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ContentProcessingMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ContentProcessingMode:
    """
    v3 Code System ContentProcessingMode

      Description:  Identifies the order in which content should be
processed.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ContentProcessingMode
    """

    seql = CodeSystemConcept(
        {
            "code": "SEQL",
            "definition": "Description:The content should be processed in a sequential fashion.",
            "display": "Sequential",
        }
    )
    """
    Sequential

    Description:The content should be processed in a sequential fashion.
    """

    unor = CodeSystemConcept(
        {
            "code": "UNOR",
            "definition": "Description:The content may be processed in any order.",
            "display": "Unordered",
        }
    )
    """
    Unordered

    Description:The content may be processed in any order.
    """

    class Meta:
        resource = _resource
