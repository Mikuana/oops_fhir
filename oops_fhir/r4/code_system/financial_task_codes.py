from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FinancialTaskCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FinancialTaskCodes:
    """
    Financial Task Codes

    This value set includes Financial Task codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/financialtaskcode
    """

    cancel = CodeSystemConcept(
        {
            "code": "cancel",
            "definition": "Cancel or reverse a resource, such as a claim or preauthorization, which is in-process or complete.",
            "display": "Cancel",
        }
    )
    """
    Cancel

    Cancel or reverse a resource, such as a claim or preauthorization, which is in-process or complete.
    """

    poll = CodeSystemConcept(
        {
            "code": "poll",
            "definition": "Retrieve selected or all queued resources or messages.",
            "display": "Poll",
        }
    )
    """
    Poll

    Retrieve selected or all queued resources or messages.
    """

    release = CodeSystemConcept(
        {
            "code": "release",
            "definition": "Release any reserved funds or material obligations associated with a resource. For example, any unused but reserved funds or treatment allowance associated with a preauthorization once treatment is complete.",
            "display": "Release",
        }
    )
    """
    Release

    Release any reserved funds or material obligations associated with a resource. For example, any unused but reserved funds or treatment allowance associated with a preauthorization once treatment is complete.
    """

    reprocess = CodeSystemConcept(
        {
            "code": "reprocess",
            "definition": "Indication that the processing of a resource, such as a claim, for some or all of the required work is now being requested.",
            "display": "Reprocess",
        }
    )
    """
    Reprocess

    Indication that the processing of a resource, such as a claim, for some or all of the required work is now being requested.
    """

    status = CodeSystemConcept(
        {
            "code": "status",
            "definition": "Check on the processing status of a resource such as the adjudication of a claim.",
            "display": "Status check",
        }
    )
    """
    Status check

    Check on the processing status of a resource such as the adjudication of a claim.
    """

    class Meta:
        resource = _resource
