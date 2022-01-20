from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["TypeRestfulInteraction"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TypeRestfulInteraction(ValueSet):
    """
    TypeRestfulInteraction

    Operations supported by REST at the type or instance level.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/type-restful-interaction
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
