from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.intervention_codes import (
    InterventionCodes as InterventionCodes_,
)


__all__ = ["InterventionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class InterventionCodes(InterventionCodes_):
    """
    Intervention Codes

    This value set includes sample Intervention codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/intervention
    """

    class Meta:
        resource = _resource
