from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.status import status as status_


__all__ = ["status"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class status(status_):
    """
    Status

    The validation status of the target

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/verificationresult-status
    """

    class Meta:
        resource = _resource
