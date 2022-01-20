from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.teeth_codes import TeethCodes as TeethCodes_


__all__ = ["TeethCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TeethCodes(TeethCodes_):
    """
    Teeth Codes

    This value set includes the FDI Teeth codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/teeth
    """

    class Meta:
        resource = _resource
