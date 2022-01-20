from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3ConfidentialityClassification"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ConfidentialityClassification(ValueSet):
    """
    V3 Value SetConfidentialityClassification

     Set of codes used to value Act.Confidentiality and Role.Confidentiality
attribute in accordance with the definition for concept domain
"Confidentiality".

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ConfidentialityClassification
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
