from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.usclscodes import USCLSCodes as USCLSCodes_


__all__ = ["USCLSCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class USCLSCodes(USCLSCodes_):
    """
    USCLS Codes

    This value set includes a smattering of USCLS codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/service-uscls
    """

    class Meta:
        resource = _resource
