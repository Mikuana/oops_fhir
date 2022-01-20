from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["LOINCDiagnosticReportCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class LOINCDiagnosticReportCodes(ValueSet):
    """
    LOINC Diagnostic Report Codes

    This value set includes LOINC codes that relate to Diagnostic
Observations.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/report-codes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
