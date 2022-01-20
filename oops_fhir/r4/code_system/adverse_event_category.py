from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventCategory:
    """
    AdverseEventCategory

    Overall categorization of the event, e.g. product-related or
situational.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/adverse-event-category
    """

    product_problem = CodeSystemConcept(
        {
            "code": "product-problem",
            "definition": "The adverse event pertains to a product problem.",
            "display": "Product Problem",
        }
    )
    """
    Product Problem

    The adverse event pertains to a product problem.
    """

    product_quality = CodeSystemConcept(
        {
            "code": "product-quality",
            "definition": "The adverse event pertains to product quality.",
            "display": "Product Quality",
        }
    )
    """
    Product Quality

    The adverse event pertains to product quality.
    """

    product_use_error = CodeSystemConcept(
        {
            "code": "product-use-error",
            "concept": [
                {
                    "code": "wrong-dose",
                    "definition": "The adverse event pertains to a wrong dose.",
                    "display": "Wrong Dose",
                },
                {
                    "code": "incorrect-prescribing-information",
                    "definition": "The adverse event pertains to incorrect perscribing information.",
                    "display": "Incorrect Prescribing Information",
                },
                {
                    "code": "wrong-technique",
                    "definition": "The adverse event pertains to a wrong technique.",
                    "display": "Wrong Technique",
                },
                {
                    "code": "wrong-route-of-administration",
                    "definition": "The adverse event pertains to a wrong route of administration.",
                    "display": "Wrong Route of Administration",
                },
                {
                    "code": "wrong-rate",
                    "definition": "The adverse event pertains to a wrong rate.",
                    "display": "Wrong Rate",
                },
                {
                    "code": "wrong-duration",
                    "definition": "The adverse event pertains to a wrong duration.",
                    "display": "Wrong Duration",
                },
                {
                    "code": "wrong-time",
                    "definition": "The adverse event pertains to a wrong time.",
                    "display": "Wrong Time",
                },
                {
                    "code": "expired-drug",
                    "definition": "The adverse event pertains to an expired drug.",
                    "display": "Expired Drug",
                },
            ],
            "definition": "The adverse event pertains to a product use error.",
            "display": "Product Use Error",
        }
    )
    """
    Product Use Error

    The adverse event pertains to a product use error.
    """

    medical_device_use_error = CodeSystemConcept(
        {
            "code": "medical-device-use-error",
            "definition": "The adverse event pertains to a medical device use error.",
            "display": "Medical Device Use Error",
        }
    )
    """
    Medical Device Use Error

    The adverse event pertains to a medical device use error.
    """

    problem_different_manufacturer = CodeSystemConcept(
        {
            "code": "problem-different-manufacturer",
            "definition": "The adverse event pertains to a problem with a different manufacturer of the same medication.",
            "display": "Problem with Different Manufacturer of Same Medicine",
        }
    )
    """
    Problem with Different Manufacturer of Same Medicine

    The adverse event pertains to a problem with a different manufacturer of the same medication.
    """

    unsafe_physical_environment = CodeSystemConcept(
        {
            "code": "unsafe-physical-environment",
            "definition": "The adverse event pertains to an unsafe physical environment.",
            "display": "Unsafe Physical Environment",
        }
    )
    """
    Unsafe Physical Environment

    The adverse event pertains to an unsafe physical environment.
    """

    class Meta:
        resource = _resource
