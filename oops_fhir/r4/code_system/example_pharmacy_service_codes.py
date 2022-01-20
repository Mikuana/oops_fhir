from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExamplePharmacyServiceCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExamplePharmacyServiceCodes:
    """
    Example Pharmacy Service Codes

    This value set includes a smattering of Pharmacy Service codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/ex-pharmaservice
    """

    smokecess = CodeSystemConcept(
        {
            "code": "smokecess",
            "definition": "Smoking cessation",
            "display": "Smoking cessation",
        }
    )
    """
    Smoking cessation

    Smoking cessation
    """

    flushot = CodeSystemConcept(
        {"code": "flushot", "definition": "Flu Shot", "display": "Flu Shot"}
    )
    """
    Flu Shot

    Flu Shot
    """

    drugcost = CodeSystemConcept(
        {
            "code": "drugcost",
            "definition": "The wholesale price of the medication.",
            "display": "Drug Cost",
        }
    )
    """
    Drug Cost

    The wholesale price of the medication.
    """

    markup = CodeSystemConcept(
        {
            "code": "markup",
            "definition": "The additional cost assessed on the drug.",
            "display": "Markup",
        }
    )
    """
    Markup

    The additional cost assessed on the drug.
    """

    dispensefee = CodeSystemConcept(
        {
            "code": "dispensefee",
            "definition": "The professional fee charged for dispensing the product or service.",
            "display": "Dispense Fee",
        }
    )
    """
    Dispense Fee

    The professional fee charged for dispensing the product or service.
    """

    compoundfee = CodeSystemConcept(
        {
            "code": "compoundfee",
            "definition": "The professional fee charged for compounding the medication.",
            "display": "Compounding Fee",
        }
    )
    """
    Compounding Fee

    The professional fee charged for compounding the medication.
    """

    class Meta:
        resource = _resource
