from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CertaintySubcomponentType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CertaintySubcomponentType:
    """
    CertaintySubcomponentType

    The subcomponent classification of quality of evidence rating systems.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/certainty-subcomponent-type
    """

    risk_of_bias = CodeSystemConcept(
        {
            "code": "RiskOfBias",
            "definition": "methodologic concerns reducing internal validity.",
            "display": "Risk of bias",
        }
    )
    """
    Risk of bias

    methodologic concerns reducing internal validity.
    """

    inconsistency = CodeSystemConcept(
        {
            "code": "Inconsistency",
            "definition": "concerns that findings are not similar enough to support certainty.",
            "display": "Inconsistency",
        }
    )
    """
    Inconsistency

    concerns that findings are not similar enough to support certainty.
    """

    indirectness = CodeSystemConcept(
        {
            "code": "Indirectness",
            "definition": "concerns reducing external validity.",
            "display": "Indirectness",
        }
    )
    """
    Indirectness

    concerns reducing external validity.
    """

    imprecision = CodeSystemConcept(
        {
            "code": "Imprecision",
            "definition": "High quality evidence.",
            "display": "Imprecision",
        }
    )
    """
    Imprecision

    High quality evidence.
    """

    publication_bias = CodeSystemConcept(
        {
            "code": "PublicationBias",
            "definition": "likelihood that what is published misrepresents what is available to publish.",
            "display": "Publication bias",
        }
    )
    """
    Publication bias

    likelihood that what is published misrepresents what is available to publish.
    """

    dose_response_gradient = CodeSystemConcept(
        {
            "code": "DoseResponseGradient",
            "definition": "higher certainty due to dose response relationship.",
            "display": "Dose response gradient",
        }
    )
    """
    Dose response gradient

    higher certainty due to dose response relationship.
    """

    plausible_confounding = CodeSystemConcept(
        {
            "code": "PlausibleConfounding",
            "definition": "higher certainty due to risk of bias in opposite direction.",
            "display": "Plausible confounding",
        }
    )
    """
    Plausible confounding

    higher certainty due to risk of bias in opposite direction.
    """

    large_effect = CodeSystemConcept(
        {
            "code": "LargeEffect",
            "definition": "higher certainty due to large effect size.",
            "display": "Large effect",
        }
    )
    """
    Large effect

    higher certainty due to large effect size.
    """

    class Meta:
        resource = _resource
