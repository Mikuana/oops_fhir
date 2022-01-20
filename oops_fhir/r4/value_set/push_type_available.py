from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.push_type_available import (
    pushtypeavailable as pushtypeavailable_,
)


__all__ = ["pushtypeavailable"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class pushtypeavailable(pushtypeavailable_):
    """
    Push-type-available

    Type of alerts/updates the primary source can send

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-push-type-available
    """

    class Meta:
        resource = _resource
