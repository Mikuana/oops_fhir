from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.data_absent_reason import (
    DataAbsentReason as DataAbsentReason_,
)


__all__ = ["DataAbsentReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DataAbsentReason(DataAbsentReason_):
    """
    DataAbsentReason

    Used to specify why the normally expected content of the data element is
missing.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/data-absent-reason
    """

    class Meta:
        resource = _resource
