from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.dicom_audit_message_record_lifecycle_events import (
    DICOMAuditMessageRecordLifecycleEvents,
)

from oops_fhir.r4.code_system.iso_21089_2017_health_record_lifecycle_events import (
    ISO210892017HealthRecordLifecycleEvents,
)


__all__ = ["ObjectLifecycleEvents"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObjectLifecycleEvents(ValueSet):
    """
    ObjectLifecycleEvents

    This example FHIR value set is comprised of lifecycle event codes. The
FHIR Actor value set is based on    DICOM Audit Message,
ParticipantObjectDataLifeCycle;   ISO Standard, TS 21089-2017;

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/object-lifecycle-events
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
