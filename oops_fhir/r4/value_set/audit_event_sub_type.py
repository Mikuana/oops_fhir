from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.fhir_restful_interactions import FHIRRestfulInteractions


__all__ = ["AuditEventSubType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventSubType(ValueSet):
    """
    Audit Event Sub-Type

    More detailed code concerning the type of the audit event - defined by
DICOM with some FHIR specific additions.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/audit-event-sub-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
