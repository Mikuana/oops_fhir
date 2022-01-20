from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestScriptProfileDestinationType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptProfileDestinationType:
    """
    Test script profile destination type

    This value set defines a set of codes that are used to indicate the
profile type of a test system when acting as the destination within a
TestScript.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/testscript-profile-destination-types
    """

    fhir_server = CodeSystemConcept(
        {
            "code": "FHIR-Server",
            "definition": "General FHIR server used to respond to operations sent from a FHIR client.",
            "display": "FHIR Server",
        }
    )
    """
    FHIR Server

    General FHIR server used to respond to operations sent from a FHIR client.
    """

    fhir_sdc_form_manager = CodeSystemConcept(
        {
            "code": "FHIR-SDC-FormManager",
            "definition": "A FHIR server acting as a Structured Data Capture Form Manager.",
            "display": "FHIR SDC FormManager",
        }
    )
    """
    FHIR SDC FormManager

    A FHIR server acting as a Structured Data Capture Form Manager.
    """

    fhir_sdc_form_processor = CodeSystemConcept(
        {
            "code": "FHIR-SDC-FormProcessor",
            "definition": "A FHIR server acting as a Structured Data Capture Form Processor.",
            "display": "FHIR SDC FormProcessor",
        }
    )
    """
    FHIR SDC FormProcessor

    A FHIR server acting as a Structured Data Capture Form Processor.
    """

    fhir_sdc_form_receiver = CodeSystemConcept(
        {
            "code": "FHIR-SDC-FormReceiver",
            "definition": "A FHIR server acting as a Structured Data Capture Form Receiver.",
            "display": "FHIR SDC FormReceiver",
        }
    )
    """
    FHIR SDC FormReceiver

    A FHIR server acting as a Structured Data Capture Form Receiver.
    """

    class Meta:
        resource = _resource
