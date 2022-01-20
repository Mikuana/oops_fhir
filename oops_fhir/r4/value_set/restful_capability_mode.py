from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.restful_capability_mode import (
    RestfulCapabilityMode as RestfulCapabilityMode_,
)


__all__ = ["RestfulCapabilityMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class RestfulCapabilityMode(RestfulCapabilityMode_):
    """
    RestfulCapabilityMode

    The mode of a RESTful capability statement.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/restful-capability-mode
    """

    class Meta:
        resource = _resource
