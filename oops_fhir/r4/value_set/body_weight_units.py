from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["BodyWeightUnits"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class BodyWeightUnits(ValueSet):
    """
    Body Weight Units

    UCUM units for recording Body Weight

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ucum-bodyweight
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
