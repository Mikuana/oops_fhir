from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ProcessingMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ProcessingMode:
    """
    v3 Code System ProcessingMode

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ProcessingMode
    """

    a = CodeSystemConcept(
        {
            "code": "A",
            "definition": "Identifies archive mode of processing.",
            "display": "Archive",
        }
    )
    """
    Archive

    Identifies archive mode of processing.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "Identifies initial load mode of processing.",
            "display": "Initial load",
        }
    )
    """
    Initial load

    Identifies initial load mode of processing.
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Identifies restore mode of processing.",
            "display": "Restore from archive",
        }
    )
    """
    Restore from archive

    Identifies restore mode of processing.
    """

    t = CodeSystemConcept(
        {
            "code": "T",
            "definition": "Identifies on-line mode of processing.",
            "display": "Current processing",
        }
    )
    """
    Current processing

    Identifies on-line mode of processing.
    """

    class Meta:
        resource = _resource
