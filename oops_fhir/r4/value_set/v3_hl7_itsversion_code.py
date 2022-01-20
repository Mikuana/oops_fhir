from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_itsversion_code import (
    v3hl7ITSVersionCode as v3hl7ITSVersionCode_,
)


__all__ = ["v3hl7ITSVersionCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7ITSVersionCode(v3hl7ITSVersionCode_):
    """
    v3 Code System hl7ITSVersionCode

     HL7 implementation technology specification versions. These codes will
document the ITS type and version for message encoding. The code will
appear in the instances based upon rules expressed in the ITS, and do
not appear in the abstract message, either as it is presented to
received from the ITS.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7ITSVersionCode
    """

    class Meta:
        resource = _resource
