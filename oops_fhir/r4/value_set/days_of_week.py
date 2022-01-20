from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.days_of_week import DaysOfWeek as DaysOfWeek_


__all__ = ["DaysOfWeek"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DaysOfWeek(DaysOfWeek_):
    """
    DaysOfWeek

    The days of the week.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/days-of-week
    """

    class Meta:
        resource = _resource
