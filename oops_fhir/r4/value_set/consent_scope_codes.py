from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_scope_codes import (
    ConsentScopeCodes as ConsentScopeCodes_,
)


__all__ = ["ConsentScopeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentScopeCodes(ConsentScopeCodes_):
    """
    Consent Scope Codes

    This value set includes the four Consent scope codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-scope
    """

    class Meta:
        resource = _resource
