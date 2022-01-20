from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_id import AuditEventID as AuditEventID_

from oops_fhir.r4.code_system.iso_21089_2017_health_record_lifecycle_events import (
    ISO210892017HealthRecordLifecycleEvents,
)


__all__ = ["AuditEventID"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventID(ValueSet):
    """
    Audit Event ID

    Event Types for Audit Events - defined by DICOM with some FHIR specific
additions.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/audit-event-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
