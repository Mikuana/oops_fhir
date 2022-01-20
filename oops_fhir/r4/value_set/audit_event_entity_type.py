from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_entity_type import (
    AuditEventEntityType as AuditEventEntityType_,
)

from oops_fhir.r4.code_system.resource_type import ResourceType


__all__ = ["AuditEventEntityType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventEntityType(ValueSet):
    """
    Audit event entity type

    Code for the entity type involved in the audit event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/audit-entity-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
