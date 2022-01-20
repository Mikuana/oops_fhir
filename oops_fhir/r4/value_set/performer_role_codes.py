from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.performer_role_codes import (
    PerformerRoleCodes as PerformerRoleCodes_,
)


__all__ = ["PerformerRoleCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class PerformerRoleCodes(PerformerRoleCodes_):
    """
    Performer Role Codes

    This value set includes sample Performer Role codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-performer
    """

    class Meta:
        resource = _resource
