from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["TimingAbbreviation"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TimingAbbreviation(ValueSet):
    """
    TimingAbbreviation

    Code for a known / defined timing pattern.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/timing-abbreviation
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
