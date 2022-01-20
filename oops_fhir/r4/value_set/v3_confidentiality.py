from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_confidentiality import (
    v3Confidentiality as v3Confidentiality_,
)


__all__ = ["v3Confidentiality"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Confidentiality(v3Confidentiality_):
    """
    v3 Code System Confidentiality

     A set of codes specifying the security classification of acts and roles
in accordance with the definition for concept domain "Confidentiality".

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-Confidentiality
    """

    class Meta:
        resource = _resource
