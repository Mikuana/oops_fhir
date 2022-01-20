from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceType:
    """
    AllergyIntoleranceType

    Identification of the underlying physiological mechanism for a Reaction
Risk.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/allergy-intolerance-type
    """

    allergy = CodeSystemConcept(
        {
            "code": "allergy",
            "definition": 'A propensity for hypersensitive reaction(s) to a substance.  These reactions are most typically type I hypersensitivity, plus other "allergy-like" reactions, including pseudoallergy.',
            "display": "Allergy",
        }
    )
    """
    Allergy

    A propensity for hypersensitive reaction(s) to a substance.  These reactions are most typically type I hypersensitivity, plus other "allergy-like" reactions, including pseudoallergy.
    """

    intolerance = CodeSystemConcept(
        {
            "code": "intolerance",
            "definition": 'A propensity for adverse reactions to a substance that is not judged to be allergic or "allergy-like".  These reactions are typically (but not necessarily) non-immune.  They are to some degree idiosyncratic and/or patient-specific (i.e. are not a reaction that is expected to occur with most or all patients given similar circumstances).',
            "display": "Intolerance",
        }
    )
    """
    Intolerance

    A propensity for adverse reactions to a substance that is not judged to be allergic or "allergy-like".  These reactions are typically (but not necessarily) non-immune.  They are to some degree idiosyncratic and/or patient-specific (i.e. are not a reaction that is expected to occur with most or all patients given similar circumstances).
    """

    class Meta:
        resource = _resource
