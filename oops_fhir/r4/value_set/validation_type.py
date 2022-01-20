from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.validation_type import validationtype as validationtype_


__all__ = ["validationtype"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class validationtype(validationtype_):
    """
    Validation-type

    What the target is validated against

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-validation-type
    """

    class Meta:
        resource = _resource
