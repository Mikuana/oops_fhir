from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["Iso316612"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Iso316612(ValueSet):
    """
    Iso 3166 Part 1: 2 Letter Codes

    This value set defines the ISO 3166 Part 1 2-letter codes

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/iso3166-1-2
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
