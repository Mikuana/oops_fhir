from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["Iso31661N"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Iso31661N(ValueSet):
    """
    Iso 3166 Part 1: Numeric Codes

    This value set defines the ISO 3166 Part 1 Numeric codes

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/iso3166-1-N
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
