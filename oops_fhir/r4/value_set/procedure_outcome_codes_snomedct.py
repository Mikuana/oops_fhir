from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ProcedureOutcomeCodesSNOMEDCT"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureOutcomeCodesSNOMEDCT(ValueSet):
    """
    Procedure Outcome Codes (SNOMED CT)

    Procedure Outcome code: A selection of relevant SNOMED CT codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/procedure-outcome
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
