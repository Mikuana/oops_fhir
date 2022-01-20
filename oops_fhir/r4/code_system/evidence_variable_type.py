from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EvidenceVariableType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EvidenceVariableType:
    """
    EvidenceVariableType

    The possible types of variables for exposures or outcomes (E.g.
Dichotomous, Continuous, Descriptive).

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/variable-type
    """

    dichotomous = CodeSystemConcept(
        {
            "code": "dichotomous",
            "definition": "The variable is dichotomous, such as present or absent.",
            "display": "Dichotomous",
        }
    )
    """
    Dichotomous

    The variable is dichotomous, such as present or absent.
    """

    continuous = CodeSystemConcept(
        {
            "code": "continuous",
            "definition": "The variable is a continuous result such as a quantity.",
            "display": "Continuous",
        }
    )
    """
    Continuous

    The variable is a continuous result such as a quantity.
    """

    descriptive = CodeSystemConcept(
        {
            "code": "descriptive",
            "definition": "The variable is described narratively rather than quantitatively.",
            "display": "Descriptive",
        }
    )
    """
    Descriptive

    The variable is described narratively rather than quantitatively.
    """

    class Meta:
        resource = _resource
