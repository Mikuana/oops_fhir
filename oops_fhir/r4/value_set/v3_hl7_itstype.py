from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_itstype import v3hl7ITSType as v3hl7ITSType_


__all__ = ["v3hl7ITSType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7ITSType(v3hl7ITSType_):
    """
    v3 Code System hl7ITSType

      Description:  Codes identifying types of HL7 Implementation Technology
Specifications

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7ITSType
    """

    class Meta:
        resource = _resource
