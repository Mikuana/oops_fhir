from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_class import v3ActClass


__all__ = ["v3ActClassClinicalDocument"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActClassClinicalDocument(v3ActClass):
    """
    V3 Value SetActClassClinicalDocument

     A clinical document is a documentation of clinical observations and
services, with the following characteristics: (1) Persistence - A
clinical document continues to exist in an unaltered state, for a time
period defined by local and regulatory requirements; (2) Stewardship - A
clinical document is maintained by a person or organization entrusted
with its care; (3) Potential for authentication - A clinical document is
an assemblage of information that is intended to be legally
authenticated; (4) Wholeness - Authentication of a clinical document
applies to the whole and does not apply to portions of the document
without the full context of the document; (5) Human readability - A
clinical document is human readable."

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActClassClinicalDocument
    """

    class Meta:
        resource = _resource
