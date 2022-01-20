from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["AllSecurityLabels"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllSecurityLabels(ValueSet):
    """
    SecurityLabels

    A single value set for all security labels defined by FHIR.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/security-labels
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
