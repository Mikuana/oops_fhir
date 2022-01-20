from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_calendar_cycle import (
    v3CalendarCycle as v3CalendarCycle_,
)


__all__ = ["v3CalendarCycle"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3CalendarCycle(v3CalendarCycle_):
    """
    v3 Code System CalendarCycle

     Calendar cycle identifiers

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-CalendarCycle
    """

    class Meta:
        resource = _resource
