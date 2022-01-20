from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_response_modality import (
    v3ResponseModality as v3ResponseModality_,
)


__all__ = ["v3ResponseModality"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ResponseModality(v3ResponseModality_):
    """
    v3 Code System ResponseModality

     Defines the timing and grouping of the response instances.  OpenIssue:
Description copied from Concept Domain of same name.  Must be verified.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ResponseModality
    """

    class Meta:
        resource = _resource
