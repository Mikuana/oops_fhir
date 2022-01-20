from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.specimen_status import SpecimenStatus as SpecimenStatus_


__all__ = ["SpecimenStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SpecimenStatus(SpecimenStatus_):
    """
    SpecimenStatus

    Codes providing the status/availability of a specimen.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/specimen-status
    """

    class Meta:
        resource = _resource
