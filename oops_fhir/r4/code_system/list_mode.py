from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ListMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ListMode:
    """
    ListMode

    The processing mode that applies to this list.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/list-mode
    """

    working = CodeSystemConcept(
        {
            "code": "working",
            "definition": "This list is the master list, maintained in an ongoing fashion with regular updates as the real world list it is tracking changes.",
            "display": "Working List",
        }
    )
    """
    Working List

    This list is the master list, maintained in an ongoing fashion with regular updates as the real world list it is tracking changes.
    """

    snapshot = CodeSystemConcept(
        {
            "code": "snapshot",
            "definition": "This list was prepared as a snapshot. It should not be assumed to be current.",
            "display": "Snapshot List",
        }
    )
    """
    Snapshot List

    This list was prepared as a snapshot. It should not be assumed to be current.
    """

    changes = CodeSystemConcept(
        {
            "code": "changes",
            "definition": "A point-in-time list that shows what changes have been made or recommended.  E.g. a discharge medication list showing what was added and removed during an encounter.",
            "display": "Change List",
        }
    )
    """
    Change List

    A point-in-time list that shows what changes have been made or recommended.  E.g. a discharge medication list showing what was added and removed during an encounter.
    """

    class Meta:
        resource = _resource
