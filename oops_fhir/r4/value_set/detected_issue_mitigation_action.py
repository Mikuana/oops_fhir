from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["DetectedIssueMitigationAction"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DetectedIssueMitigationAction(v3ActCode):
    """
    Detected Issue Mitigation Action

    Kinds of mitigating actions and observations that can be associated with
a detected issue or contraindication, such as 'added concurrent
therapy', 'prior therapy documented', etc.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/detectedissue-mitigation-action
    """

    class Meta:
        resource = _resource
