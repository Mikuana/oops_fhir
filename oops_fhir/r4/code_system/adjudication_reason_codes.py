from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdjudicationReasonCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdjudicationReasonCodes:
    """
    Adjudication Reason Codes

    This value set includes smattering of Adjudication Reason codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/adjudication-reason
    """

    ar001 = CodeSystemConcept(
        {"code": "ar001", "definition": "Not covered", "display": "Not covered"}
    )
    """
    Not covered

    Not covered
    """

    ar002 = CodeSystemConcept(
        {
            "code": "ar002",
            "definition": "Plan Limit Reached",
            "display": "Plan Limit Reached",
        }
    )
    """
    Plan Limit Reached

    Plan Limit Reached
    """

    class Meta:
        resource = _resource
