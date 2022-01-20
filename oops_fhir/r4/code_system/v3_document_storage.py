from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3DocumentStorage"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3DocumentStorage:
    """
    v3 Code System DocumentStorage

     Identifies the storage status of a document.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-DocumentStorage
    """

    ac = CodeSystemConcept(
        {
            "code": "AC",
            "concept": [
                {
                    "code": "AA",
                    "definition": "A storage status in which a document is available on-line and is also stored off-line for long-term access.",
                    "display": "active and archived",
                }
            ],
            "definition": "A storage status in which a document is available on-line.",
            "display": "active",
        }
    )
    """
    active

    A storage status in which a document is available on-line.
    """

    ar = CodeSystemConcept(
        {
            "code": "AR",
            "definition": "A storage status in which a document has been stored off-line for long-term access.",
            "display": "archived (not active)",
        }
    )
    """
    archived (not active)

    A storage status in which a document has been stored off-line for long-term access.
    """

    pu = CodeSystemConcept(
        {
            "code": "PU",
            "definition": "A storage status in which a document is no longer available in this system.",
            "display": "purged",
        }
    )
    """
    purged

    A storage status in which a document is no longer available in this system.
    """

    class Meta:
        resource = _resource
