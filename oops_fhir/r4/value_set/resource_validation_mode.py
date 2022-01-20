from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.resource_validation_mode import (
    ResourceValidationMode as ResourceValidationMode_,
)


__all__ = ["ResourceValidationMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ResourceValidationMode(ResourceValidationMode_):
    """
    ResourceValidationMode

    Codes indicating the type of validation to perform.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/resource-validation-mode
    """

    class Meta:
        resource = _resource
