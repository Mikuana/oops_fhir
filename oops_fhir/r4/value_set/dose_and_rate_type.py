from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.dose_and_rate_type import (
    DoseAndRateType as DoseAndRateType_,
)


__all__ = ["DoseAndRateType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DoseAndRateType(DoseAndRateType_):
    """
    DoseAndRateType

    The kind of dose or rate specified.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/dose-rate-type
    """

    class Meta:
        resource = _resource
