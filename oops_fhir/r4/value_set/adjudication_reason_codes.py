from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adjudication_reason_codes import (
    AdjudicationReasonCodes as AdjudicationReasonCodes_,
)


__all__ = ["AdjudicationReasonCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdjudicationReasonCodes(AdjudicationReasonCodes_):
    """
    Adjudication Reason Codes

    This value set includes smattering of Adjudication Reason codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adjudication-reason
    """

    class Meta:
        resource = _resource
