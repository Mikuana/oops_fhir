from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ServiceProvisionConditions"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ServiceProvisionConditions:
    """
    ServiceProvisionConditions

    The code(s) that detail the conditions under which the healthcare
service is available/offered.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/service-provision-conditions
    """

    free = CodeSystemConcept(
        {
            "code": "free",
            "definition": "This service is available for no patient cost.",
            "display": "Free",
        }
    )
    """
    Free

    This service is available for no patient cost.
    """

    disc = CodeSystemConcept(
        {
            "code": "disc",
            "definition": "There are discounts available on this service for qualifying patients.",
            "display": "Discounts Available",
        }
    )
    """
    Discounts Available

    There are discounts available on this service for qualifying patients.
    """

    cost = CodeSystemConcept(
        {
            "code": "cost",
            "definition": "Fees apply for this service.",
            "display": "Fees apply",
        }
    )
    """
    Fees apply

    Fees apply for this service.
    """

    class Meta:
        resource = _resource
