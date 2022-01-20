from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_source_type import (
    AuditEventSourceType as AuditEventSourceType_,
)


__all__ = ["AuditEventSourceType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventSourceType(AuditEventSourceType_):
    """
    Audit Event Source Type

    The type of process where the audit event originated from.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/audit-source-type
    """

    class Meta:
        resource = _resource
