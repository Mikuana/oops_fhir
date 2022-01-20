from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceSubstanceExposureRisk"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceSubstanceExposureRisk:
    """
    AllergyIntoleranceSubstanceExposureRisk

    The risk of an adverse reaction (allergy or intolerance) for this
patient upon exposure to the substance (including pharmaceutical
products).

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk
    """

    known_reaction_risk = CodeSystemConcept(
        {
            "code": "known-reaction-risk",
            "definition": "Known risk of allergy or intolerance reaction upon exposure to the specified substance.",
            "display": "Known Reaction Risk",
        }
    )
    """
    Known Reaction Risk

    Known risk of allergy or intolerance reaction upon exposure to the specified substance.
    """

    no_known_reaction_risk = CodeSystemConcept(
        {
            "code": "no-known-reaction-risk",
            "definition": "No known risk of allergy or intolerance reaction upon exposure to the specified substance.",
            "display": "No Known Reaction Risk",
        }
    )
    """
    No Known Reaction Risk

    No known risk of allergy or intolerance reaction upon exposure to the specified substance.
    """

    class Meta:
        resource = _resource
