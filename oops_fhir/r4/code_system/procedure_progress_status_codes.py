from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ProcedureProgressStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureProgressStatusCodes:
    """
    Procedure Progress Status Codes

    This value set is provided as an example. The value set to instantiate
this attribute should be drawn from a robust terminology code system
that consists of or contains concepts to support the procedure
performance process.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/procedure-progress-status-code
    """

    in_operating_room = CodeSystemConcept(
        {
            "code": "in-operating-room",
            "definition": "A patient is in the Operating Room.",
            "display": "In Operating Room",
        }
    )
    """
    In Operating Room

    A patient is in the Operating Room.
    """

    prepared = CodeSystemConcept(
        {
            "code": "prepared",
            "definition": "The patient is prepared for a procedure.",
            "display": "Prepared",
        }
    )
    """
    Prepared

    The patient is prepared for a procedure.
    """

    anesthesia_induced = CodeSystemConcept(
        {
            "code": "anesthesia-induced",
            "definition": "The patient is under anesthesia.",
            "display": "Anesthesia Induced",
        }
    )
    """
    Anesthesia Induced

    The patient is under anesthesia.
    """

    open_incision = CodeSystemConcept(
        {
            "code": "open-incision",
            "definition": "The patient has open incision(s).",
            "display": "Open Incision",
        }
    )
    """
    Open Incision

    The patient has open incision(s).
    """

    closed_incision = CodeSystemConcept(
        {
            "code": "closed-incision",
            "definition": "The patient has incision(s) closed.",
            "display": "Closed Incision",
        }
    )
    """
    Closed Incision

    The patient has incision(s) closed.
    """

    in_recovery_room = CodeSystemConcept(
        {
            "code": "in-recovery-room",
            "definition": "The patient is in the recovery room.",
            "display": "In Recovery Room",
        }
    )
    """
    In Recovery Room

    The patient is in the recovery room.
    """

    class Meta:
        resource = _resource
