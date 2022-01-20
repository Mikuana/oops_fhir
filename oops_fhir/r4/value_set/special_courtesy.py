from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["SpecialCourtesy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecialCourtesy(ValueSet):
    """
    Special courtesy

    This value set defines a set of codes that can be used to indicate
special courtesies provided to the patient.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-special-courtesy
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
