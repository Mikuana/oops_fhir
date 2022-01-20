from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestScriptProfileOriginType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptProfileOriginType:
    """
    Test script profile origin type

    This value set defines a set of codes that are used to indicate the
profile type of a test system when acting as the origin within a
TestScript.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types
    """

    fhir_client = CodeSystemConcept(
        {
            "code": "FHIR-Client",
            "definition": "General FHIR client used to initiate operations against a FHIR server.",
            "display": "FHIR Client",
        }
    )
    """
    FHIR Client

    General FHIR client used to initiate operations against a FHIR server.
    """

    fhir_sdc_form_filler = CodeSystemConcept(
        {
            "code": "FHIR-SDC-FormFiller",
            "definition": "A FHIR client acting as a Structured Data Capture Form Filler.",
            "display": "FHIR SDC FormFiller",
        }
    )
    """
    FHIR SDC FormFiller

    A FHIR client acting as a Structured Data Capture Form Filler.
    """

    class Meta:
        resource = _resource
