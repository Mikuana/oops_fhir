from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass


__all__ = ["v3ActClassDocument"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClassDocument(v3ActClass):
    """
    V3 Value SetActClassDocument

     Specialization of Act to add the characteristics unique to document
management services.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActClassDocument
    """

    class Meta:
        resource = _resource
