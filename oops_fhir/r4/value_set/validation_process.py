from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.validation_process import (
    validationprocess as validationprocess_,
)


__all__ = ["validationprocess"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class validationprocess(validationprocess_):
    """
    Validation-process

    The primary process by which the target is validated

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-validation-process
    """

    class Meta:
        resource = _resource
