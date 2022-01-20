from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.device_use_statement_status import (
    DeviceUseStatementStatus as DeviceUseStatementStatus_,
)


__all__ = ["DeviceUseStatementStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DeviceUseStatementStatus(DeviceUseStatementStatus_):
    """
    DeviceUseStatementStatus

    A coded concept indicating the current status of the Device Usage.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-statement-status
    """

    class Meta:
        resource = _resource
