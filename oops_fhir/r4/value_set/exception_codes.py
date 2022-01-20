from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.exception_codes import ExceptionCodes as ExceptionCodes_


__all__ = ["ExceptionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExceptionCodes(ExceptionCodes_):
    """
    Exception Codes

    This value set includes sample Exception codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/claim-exception
    """

    class Meta:
        resource = _resource
