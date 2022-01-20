from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CoverageEligibilityResponseAuthSupportCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CoverageEligibilityResponseAuthSupportCodes:
    """
    CoverageEligibilityResponse Auth Support Codes

    This value set includes CoverageEligibilityResponse Auth Support codes.

    Status: draft - Version: 4.0.1

    Copyright HL7 Inc.

    http://terminology.hl7.org/CodeSystem/coverageeligibilityresponse-ex-auth-support
    """

    laborder = CodeSystemConcept(
        {
            "code": "laborder",
            "definition": "A request or authorization for laboratory diagnostic tests.",
            "display": "Lab Order",
        }
    )
    """
    Lab Order

    A request or authorization for laboratory diagnostic tests.
    """

    labreport = CodeSystemConcept(
        {
            "code": "labreport",
            "definition": "A report on laboratory diagnostic test(s).",
            "display": "Lab Report",
        }
    )
    """
    Lab Report

    A report on laboratory diagnostic test(s).
    """

    diagnosticimageorder = CodeSystemConcept(
        {
            "code": "diagnosticimageorder",
            "definition": "A request or authorization for diagnostic imaging.",
            "display": "Diagnostic Image Order",
        }
    )
    """
    Diagnostic Image Order

    A request or authorization for diagnostic imaging.
    """

    diagnosticimagereport = CodeSystemConcept(
        {
            "code": "diagnosticimagereport",
            "definition": "A report on diagnostic image(s).",
            "display": "Diagnostic Image Report",
        }
    )
    """
    Diagnostic Image Report

    A report on diagnostic image(s).
    """

    professionalreport = CodeSystemConcept(
        {
            "code": "professionalreport",
            "definition": "A report from a licensed professional regarding the siutation, condition or proposed treatment.",
            "display": "Professional Report",
        }
    )
    """
    Professional Report

    A report from a licensed professional regarding the siutation, condition or proposed treatment.
    """

    accidentreport = CodeSystemConcept(
        {
            "code": "accidentreport",
            "definition": "A formal accident report as would be filed with police or a simlar official body.",
            "display": "Accident Report",
        }
    )
    """
    Accident Report

    A formal accident report as would be filed with police or a simlar official body.
    """

    model = CodeSystemConcept(
        {
            "code": "model",
            "definition": "A physical model of the affected area.",
            "display": "Model",
        }
    )
    """
    Model

    A physical model of the affected area.
    """

    picture = CodeSystemConcept(
        {
            "code": "picture",
            "definition": "A photograph of the affected area.",
            "display": "Picture",
        }
    )
    """
    Picture

    A photograph of the affected area.
    """

    class Meta:
        resource = _resource
