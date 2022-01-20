from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActUncertainty"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActUncertainty:
    """
    v3 Code System ActUncertainty

      OpenIssue:  Missing Description

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActUncertainty
    """

    n = CodeSystemConcept(
        {
            "code": "N",
            "definition": "Specifies that the act statement is made without explicit tagging of uncertainty. This is the normal statement, meaning that it is not free of errors and uncertainty may still exist.",
            "display": "stated with no assertion of uncertainty",
        }
    )
    """
    stated with no assertion of uncertainty

    Specifies that the act statement is made without explicit tagging of uncertainty. This is the normal statement, meaning that it is not free of errors and uncertainty may still exist.
    """

    u = CodeSystemConcept(
        {
            "code": "U",
            "definition": "Specifies that the originator of the Act statement does not have full confidence in the applicability (i.e., in event mood: factual truth) of the statement.",
            "display": "stated with uncertainty",
        }
    )
    """
    stated with uncertainty

    Specifies that the originator of the Act statement does not have full confidence in the applicability (i.e., in event mood: factual truth) of the statement.
    """

    class Meta:
        resource = _resource
