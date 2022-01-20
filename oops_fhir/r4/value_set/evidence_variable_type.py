from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.evidence_variable_type import (
    EvidenceVariableType as EvidenceVariableType_,
)


__all__ = ["EvidenceVariableType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EvidenceVariableType(EvidenceVariableType_):
    """
    EvidenceVariableType

    The possible types of variables for exposures or outcomes (E.g.
Dichotomous, Continuous, Descriptive).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/variable-type
    """

    class Meta:
        resource = _resource
