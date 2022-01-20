from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_entity_role import (
    AuditEventEntityRole as AuditEventEntityRole_,
)


__all__ = ["AuditEventEntityRole"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventEntityRole(AuditEventEntityRole_):
    """
    AuditEventEntityRole

    Code representing the role the entity played in the audit event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/object-role
    """

    class Meta:
        resource = _resource
