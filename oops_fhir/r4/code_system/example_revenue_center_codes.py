from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExampleRevenueCenterCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExampleRevenueCenterCodes:
    """
    Example Revenue Center Codes

    This value set includes sample Revenue Center codes.

    Status: draft - Version: 4.0.1

    Copyright These codes have been appropriated from the [UB04 code set](http://www.nubc.org/) owned and managed by the [AHA](http://www.aha.org/). Users require a [license from the AHA](http://www.nubc.org/licensing/index.dhtml) in order to use these codes. **Note: the codes have been withdrawn in a later version**

    http://terminology.hl7.org/CodeSystem/ex-revenue-center
    """

    zero370 = CodeSystemConcept(
        {"code": "0370", "definition": "Anaesthesia.", "display": "Anaesthesia"}
    )
    """
    Anaesthesia

    Anaesthesia.
    """

    zero420 = CodeSystemConcept(
        {
            "code": "0420",
            "definition": "Physical Therapy.",
            "display": "Physical Therapy",
        }
    )
    """
    Physical Therapy

    Physical Therapy.
    """

    zero421 = CodeSystemConcept(
        {
            "code": "0421",
            "definition": "Physical Therapy - visit charge.",
            "display": "Physical Therapy - ",
        }
    )
    """
    Physical Therapy - 

    Physical Therapy - visit charge.
    """

    zero440 = CodeSystemConcept(
        {
            "code": "0440",
            "definition": "Speech-Language Pathology.",
            "display": "Speech-Language Pathology",
        }
    )
    """
    Speech-Language Pathology

    Speech-Language Pathology.
    """

    zero441 = CodeSystemConcept(
        {
            "code": "0441",
            "definition": "Speech-Language Pathology- visit charge",
            "display": "Speech-Language Pathology - Visit",
        }
    )
    """
    Speech-Language Pathology - Visit

    Speech-Language Pathology- visit charge
    """

    zero450 = CodeSystemConcept(
        {"code": "0450", "definition": "Emergency Room", "display": "Emergency Room"}
    )
    """
    Emergency Room

    Emergency Room
    """

    zero451 = CodeSystemConcept(
        {
            "code": "0451",
            "definition": "Emergency Room - EM/EMTALA",
            "display": "Emergency Room - EM/EMTALA",
        }
    )
    """
    Emergency Room - EM/EMTALA

    Emergency Room - EM/EMTALA
    """

    zero452 = CodeSystemConcept(
        {
            "code": "0452",
            "definition": "Emergency Room - beyond EMTALA",
            "display": "Emergency Room - beyond EMTALA",
        }
    )
    """
    Emergency Room - beyond EMTALA

    Emergency Room - beyond EMTALA
    """

    zero010 = CodeSystemConcept(
        {"code": "0010", "definition": "Vision Clinic", "display": "Vision Clinic"}
    )
    """
    Vision Clinic

    Vision Clinic
    """

    class Meta:
        resource = _resource
