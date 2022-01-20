from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ProcedureFollowUpCodesSNOMEDCT"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureFollowUpCodesSNOMEDCT(ValueSet):
    """
    Procedure Follow up Codes (SNOMED CT)

    Procedure follow up codes: A selection of SNOMED CT codes relevant to
procedure follow up.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/procedure-followup
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
