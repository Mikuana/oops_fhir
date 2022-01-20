from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.hl7_workgroup import HL7Workgroup as HL7Workgroup_


__all__ = ["HL7Workgroup"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class HL7Workgroup(HL7Workgroup_):
    """
    HL7Workgroup

    An HL7 administrative unit that owns artifacts in the FHIR
specification.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/hl7-work-group
    """

    class Meta:
        resource = _resource
