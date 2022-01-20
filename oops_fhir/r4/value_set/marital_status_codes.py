from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_marital_status import v3MaritalStatus


__all__ = ["MaritalStatusCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MaritalStatusCodes(ValueSet):
    """
    MaritalStatus

    This value set defines the set of codes that can be used to indicate the
marital status of a person.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/marital-status
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
