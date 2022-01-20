from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BenefitTermCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BenefitTermCodes:
    """
    Benefit Term Codes

    This value set includes a smattering of Benefit Term codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/benefit-term
    """

    annual = CodeSystemConcept(
        {
            "code": "annual",
            "definition": "Annual, renewing on the anniversary",
            "display": "Annual",
        }
    )
    """
    Annual

    Annual, renewing on the anniversary
    """

    day = CodeSystemConcept({"code": "day", "definition": "Per day", "display": "Day"})
    """
    Day

    Per day
    """

    lifetime = CodeSystemConcept(
        {
            "code": "lifetime",
            "definition": "For the total term, lifetime, of the policy or coverage",
            "display": "Lifetime",
        }
    )
    """
    Lifetime

    For the total term, lifetime, of the policy or coverage
    """

    class Meta:
        resource = _resource
