from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_action import (
    AuditEventAction as AuditEventAction_,
)


__all__ = ["AuditEventAction"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventAction(AuditEventAction_):
    """
    AuditEventAction

    Indicator for type of action performed during the event that generated
the event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/audit-event-action
    """

    class Meta:
        resource = _resource
