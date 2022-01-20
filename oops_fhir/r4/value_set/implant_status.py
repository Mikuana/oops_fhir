from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.implant_status import ImplantStatus as ImplantStatus_


__all__ = ["ImplantStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ImplantStatus(ImplantStatus_):
    """
    Implant Status

    A set codes that define the functional status of an implanted device.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/implantStatus
    """

    class Meta:
        resource = _resource
