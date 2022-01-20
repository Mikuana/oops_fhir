from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.flag_status import FlagStatus as FlagStatus_


__all__ = ["FlagStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FlagStatus(FlagStatus_):
    """
    FlagStatus

    Indicates whether this flag is active and needs to be displayed to a
user, or whether it is no longer needed or was entered in error.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/flag-status
    """

    class Meta:
        resource = _resource
