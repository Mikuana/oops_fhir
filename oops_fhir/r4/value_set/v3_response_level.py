from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_response_level import (
    v3ResponseLevel as v3ResponseLevel_,
)


__all__ = ["v3ResponseLevel"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ResponseLevel(v3ResponseLevel_):
    """
    v3 Code System ResponseLevel

     Specifies whether a response is expected from the addressee of this
interaction and what level of detail that response should include

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ResponseLevel
    """

    class Meta:
        resource = _resource
