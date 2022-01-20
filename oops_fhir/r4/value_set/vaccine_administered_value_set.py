from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["VaccineAdministeredValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class VaccineAdministeredValueSet(ValueSet):
    """
    Vaccine Administered Value Set

    This identifies the vaccine substance administered - CVX codes.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/vaccine-code
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
