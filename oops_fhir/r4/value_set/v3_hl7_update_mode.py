from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_update_mode import (
    v3HL7UpdateMode as v3HL7UpdateMode_,
)


__all__ = ["v3HL7UpdateMode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3HL7UpdateMode(v3HL7UpdateMode_):
    """
    v3 Code System HL7UpdateMode

     The possible modes of updating that occur when an attribute is received
by a system that already contains values for that attribute.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-HL7UpdateMode
    """

    class Meta:
        resource = _resource
