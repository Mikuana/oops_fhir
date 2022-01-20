from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["CommonUCUMCodesForDistance"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CommonUCUMCodesForDistance(ValueSet):
    """
    Common UCUM Codes for Distance

    Unified Code for Units of Measure (UCUM). This value set includes common
UCUM codes for units of distance

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/distance-units
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
