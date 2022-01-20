from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["VitalSignsUnits"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class VitalSignsUnits(ValueSet):
    """
    Vital Signs Units

    Common UCUM units for recording Vital Signs

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/ucum-vitals-common
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
