from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.communication_not_done_reason import (
    CommunicationNotDoneReason as CommunicationNotDoneReason_,
)


__all__ = ["CommunicationNotDoneReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CommunicationNotDoneReason(CommunicationNotDoneReason_):
    """
    CommunicationNotDoneReason

    Codes for the reason why a communication did not happen.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/communication-not-done-reason
    """

    class Meta:
        resource = _resource
