from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["SystemRestfulInteraction"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SystemRestfulInteraction(ValueSet):
    """
    SystemRestfulInteraction

    Operations supported by REST at the system level.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/system-restful-interaction
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
