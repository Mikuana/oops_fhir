from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.consent_state import ConsentState as ConsentState_


__all__ = ["ConsentState"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConsentState(ConsentState_):
    """
    ConsentState

    Indicates the state of the consent.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consent-state-codes
    """

    class Meta:
        resource = _resource
