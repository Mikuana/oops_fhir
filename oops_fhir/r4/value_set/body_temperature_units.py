from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["BodyTemperatureUnits"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BodyTemperatureUnits(ValueSet):
    """
    Body Temperature Units

    UCUM units for recording Body Temperature

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ucum-bodytemp
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
