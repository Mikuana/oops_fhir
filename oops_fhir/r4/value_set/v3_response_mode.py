from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_response_mode import v3ResponseMode as v3ResponseMode_


__all__ = ["v3ResponseMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ResponseMode(v3ResponseMode_):
    """
    v3 Code System ResponseMode

     Specifies the mode, immediate versus deferred or queued, by which a
receiver should communicate its receiver responsibilities.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ResponseMode
    """

    class Meta:
        resource = _resource
