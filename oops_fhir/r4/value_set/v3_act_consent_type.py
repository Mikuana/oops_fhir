from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3ActConsentType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActConsentType(v3ActCode):
    """
    V3 Value SetActConsentType

      Definition:  The type of consent directive, e.g., to consent or
dissent to collect, access, or use in specific ways within an EHRS or
for health information exchange; or to disclose  health information  for
purposes such as research.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ActConsentType
    """

    class Meta:
        resource = _resource
