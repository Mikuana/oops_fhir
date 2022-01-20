from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.eligibility_request_purpose import (
    EligibilityRequestPurpose as EligibilityRequestPurpose_,
)


__all__ = ["EligibilityRequestPurpose"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EligibilityRequestPurpose(EligibilityRequestPurpose_):
    """
    EligibilityRequestPurpose

    A code specifying the types of information being requested.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/eligibilityrequest-purpose
    """

    class Meta:
        resource = _resource
