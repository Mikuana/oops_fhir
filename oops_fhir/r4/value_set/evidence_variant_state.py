from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.evidence_variant_state import (
    EvidenceVariantState as EvidenceVariantState_,
)


__all__ = ["EvidenceVariantState"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EvidenceVariantState(EvidenceVariantState_):
    """
    EvidenceVariantState

    Used for results by exposure in variant states such as low-risk, medium-
risk and high-risk states.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/evidence-variant-state
    """

    class Meta:
        resource = _resource
