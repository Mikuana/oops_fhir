from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DiagnosticServiceSectionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DiagnosticServiceSectionCodes(ValueSet):
    """
    Diagnostic Service Section Codes

    This value set includes all the codes in HL7 V2 table 0074.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/diagnostic-service-sections
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
