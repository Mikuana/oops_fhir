from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["CommonUCUMCodesForDuration"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CommonUCUMCodesForDuration(ValueSet):
    """
    Common UCUM Codes for Duration

    Unified Code for Units of Measure (UCUM). This value set includes all
UCUM codes

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/duration-units
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
