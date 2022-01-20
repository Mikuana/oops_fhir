from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_action_codes import (
    ConsentActionCodes as ConsentActionCodes_,
)


__all__ = ["ConsentActionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentActionCodes(ConsentActionCodes_):
    """
    Consent Action Codes

    This value set includes sample Consent Action codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-action
    """

    class Meta:
        resource = _resource
