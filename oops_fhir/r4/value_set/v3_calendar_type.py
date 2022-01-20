from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_calendar_type import v3CalendarType as v3CalendarType_


__all__ = ["v3CalendarType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3CalendarType(v3CalendarType_):
    """
    v3 Code System CalendarType

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-CalendarType
    """

    class Meta:
        resource = _resource
