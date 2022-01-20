from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_outcome import (
    AuditEventOutcome as AuditEventOutcome_,
)


__all__ = ["AuditEventOutcome"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventOutcome(AuditEventOutcome_):
    """
    AuditEventOutcome

    Indicates whether the event succeeded or failed.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/audit-event-outcome
    """

    class Meta:
        resource = _resource
