from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.composition_attestation_mode import (
    CompositionAttestationMode as CompositionAttestationMode_,
)


__all__ = ["CompositionAttestationMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CompositionAttestationMode(CompositionAttestationMode_):
    """
    CompositionAttestationMode

    The way in which a person authenticated a composition.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/composition-attestation-mode
    """

    class Meta:
        resource = _resource
