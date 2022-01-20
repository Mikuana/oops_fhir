from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_standard_version_code import (
    v3HL7StandardVersionCode as v3HL7StandardVersionCode_,
)


__all__ = ["v3HL7StandardVersionCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3HL7StandardVersionCode(v3HL7StandardVersionCode_):
    """
    v3 Code System HL7StandardVersionCode

     This code system holds version codes for the Version 3 standards.
Values are to be determined by HL7 and added with each new version of
the HL7 Standard.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-HL7StandardVersionCode
    """

    class Meta:
        resource = _resource
