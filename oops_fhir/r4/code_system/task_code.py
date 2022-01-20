from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TaskCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TaskCode:
    """
    Task Codes

    Codes indicating the type of action that is expected to be performed

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/CodeSystem/task-code
    """

    approve = CodeSystemConcept(
        {
            "code": "approve",
            "definition": "Take what actions are needed to transition the focus resource from 'draft' to 'active' or 'in-progress', as appropriate for the resource type.  This may involve additing additional content, approval, validation, etc.",
            "display": "Activate/approve the focal resource",
        }
    )
    """
    Activate/approve the focal resource

    Take what actions are needed to transition the focus resource from 'draft' to 'active' or 'in-progress', as appropriate for the resource type.  This may involve additing additional content, approval, validation, etc.
    """

    fulfill = CodeSystemConcept(
        {
            "code": "fulfill",
            "definition": "Act to perform the actions defined in the focus request.  This might result in a 'more assertive' request (order for a plan or proposal, filler order for a placer order), but is intend to eventually result in events.  The degree of fulfillment requested might be limited by Task.restriction.",
            "display": "Fulfill the focal request",
        }
    )
    """
    Fulfill the focal request

    Act to perform the actions defined in the focus request.  This might result in a 'more assertive' request (order for a plan or proposal, filler order for a placer order), but is intend to eventually result in events.  The degree of fulfillment requested might be limited by Task.restriction.
    """

    abort = CodeSystemConcept(
        {
            "code": "abort",
            "definition": "Abort, cancel or withdraw the focal resource, as appropriate for the type of resource.",
            "display": "Mark the focal resource as no longer active",
        }
    )
    """
    Mark the focal resource as no longer active

    Abort, cancel or withdraw the focal resource, as appropriate for the type of resource.
    """

    replace = CodeSystemConcept(
        {
            "code": "replace",
            "definition": "Replace the focal resource with the specified input resource",
            "display": "Replace the focal resource with the input resource",
        }
    )
    """
    Replace the focal resource with the input resource

    Replace the focal resource with the specified input resource
    """

    change = CodeSystemConcept(
        {
            "code": "change",
            "definition": "Update the focal resource of the owning system to reflect the content specified as the Task.focus",
            "display": "Change the focal resource",
        }
    )
    """
    Change the focal resource

    Update the focal resource of the owning system to reflect the content specified as the Task.focus
    """

    suspend = CodeSystemConcept(
        {
            "code": "suspend",
            "definition": "Transition the focal resource from 'active' or 'in-progress' to 'suspended'",
            "display": "Suspend the focal resource",
        }
    )
    """
    Suspend the focal resource

    Transition the focal resource from 'active' or 'in-progress' to 'suspended'
    """

    resume = CodeSystemConcept(
        {
            "code": "resume",
            "definition": "Transition the focal resource from 'suspended' to 'active' or 'in-progress' as appropriate for the resource type.",
            "display": "Re-activate the focal resource",
        }
    )
    """
    Re-activate the focal resource

    Transition the focal resource from 'suspended' to 'active' or 'in-progress' as appropriate for the resource type.
    """

    class Meta:
        resource = _resource
