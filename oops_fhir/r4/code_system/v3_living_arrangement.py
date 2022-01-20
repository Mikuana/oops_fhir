from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3LivingArrangement"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3LivingArrangement:
    """
    v3 Code System LivingArrangement

     A code depicting the living arrangements of a person

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-LivingArrangement
    """

    hl = CodeSystemConcept(
        {
            "code": "HL",
            "concept": [
                {"code": "M", "definition": "Nomadic", "display": "Nomadic"},
                {"code": "T", "definition": "Transient", "display": "Transient"},
            ],
            "definition": "Definition: Living arrangements lacking a permanent residence.",
            "display": "homeless",
        }
    )
    """
    homeless

    Definition: Living arrangements lacking a permanent residence.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "concept": [
                {
                    "code": "CS",
                    "definition": "Definition: A group living arrangement specifically for the care of those in need of temporary and crisis housing assistance.  Examples include domestic violence shelters, shelters for displaced or homeless individuals, Salvation Army, Jesus House, etc.  Community based services may be provided.",
                    "display": "community shelter",
                },
                {"code": "G", "definition": "Group Home", "display": "Group Home"},
                {"code": "N", "definition": "Nursing Home", "display": "Nursing Home"},
                {
                    "code": "X",
                    "definition": "Extended care facility",
                    "display": "Extended care facility",
                },
            ],
            "definition": "Institution",
            "display": "Institution",
        }
    )
    """
    Institution

    Institution
    """

    pr = CodeSystemConcept(
        {
            "code": "PR",
            "concept": [
                {
                    "code": "H",
                    "definition": "Independent Household",
                    "display": "Independent Household",
                },
                {
                    "code": "R",
                    "definition": "Retirement Community",
                    "display": "Retirement Community",
                },
                {
                    "code": "SL",
                    "definition": "Definition: Assisted living in a single family residence for persons with physical, behavioral, or functional health, or socio-economic challenges.  There may or may not be on-site supervision but the housing is designed to assist the client with developing independent living skills. Community based services may be provided.",
                    "display": "supported living",
                },
            ],
            "definition": "Definition:  A living arrangement within a private residence for single family.",
            "display": "private residence",
        }
    )
    """
    private residence

    Definition:  A living arrangement within a private residence for single family.
    """

    class Meta:
        resource = _resource
