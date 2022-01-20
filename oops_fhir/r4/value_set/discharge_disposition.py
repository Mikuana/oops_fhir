from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.discharge_disposition import (
    DischargeDisposition as DischargeDisposition_,
)


__all__ = ["DischargeDisposition"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DischargeDisposition(DischargeDisposition_):
    """
    Discharge disposition

    This value set defines a set of codes that can be used to where the
patient left the hospital.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-discharge-disposition
    """

    class Meta:
        resource = _resource
