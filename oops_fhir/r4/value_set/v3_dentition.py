from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_dentition import v3Dentition as v3Dentition_


__all__ = ["v3Dentition"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3Dentition(v3Dentition_):
    """
    v3 Code System Dentition

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-Dentition
    """

    class Meta:
        resource = _resource
