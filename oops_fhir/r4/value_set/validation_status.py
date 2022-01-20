from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.validation_status import (
    validationstatus as validationstatus_,
)


__all__ = ["validationstatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class validationstatus(validationstatus_):
    """
    Validation-status

    Status of the validation of the target against the primary source

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-validation-status
    """

    class Meta:
        resource = _resource
