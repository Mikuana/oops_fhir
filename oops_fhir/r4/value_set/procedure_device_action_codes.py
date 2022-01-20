from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["ProcedureDeviceActionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcedureDeviceActionCodes(SNOMEDCT):
    """
    Procedure Device Action Codes

    Example codes indicating the change that happened to the device during
the procedure.  Note that these are in no way complete and might not
even be appropriate for some uses.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/device-action
    """

    class Meta:
        resource = _resource
