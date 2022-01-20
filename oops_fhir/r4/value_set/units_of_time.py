from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["UnitsOfTime"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class UnitsOfTime(ValueSet):
    """
    UnitsOfTime

    A unit of time (units from UCUM).

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/units-of-time
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
