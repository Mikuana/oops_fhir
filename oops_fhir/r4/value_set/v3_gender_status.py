from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_gender_status import v3GenderStatus as v3GenderStatus_


__all__ = ["v3GenderStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3GenderStatus(v3GenderStatus_):
    """
    v3 Code System GenderStatus

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-GenderStatus
    """

    class Meta:
        resource = _resource
