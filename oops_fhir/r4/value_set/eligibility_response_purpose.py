from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.eligibility_response_purpose import (
    EligibilityResponsePurpose as EligibilityResponsePurpose_,
)


__all__ = ["EligibilityResponsePurpose"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EligibilityResponsePurpose(EligibilityResponsePurpose_):
    """
    EligibilityResponsePurpose

    A code specifying the types of information being requested.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/eligibilityresponse-purpose
    """

    class Meta:
        resource = _resource
