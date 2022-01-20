from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["DetectedIssueCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DetectedIssueCategory(ValueSet):
    """
    Detected Issue Category

    Kinds of issues or contraindications, such as 'drug-drug interaction',
'duplicate therapy', etc.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/detectedissue-category
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
