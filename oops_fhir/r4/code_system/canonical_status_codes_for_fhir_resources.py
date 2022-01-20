from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CanonicalStatusCodesforFHIRResources"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CanonicalStatusCodesforFHIRResources:
    """
    None

    The master set of status codes used throughout FHIR. All status codes
are mapped to one of these codes.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/resource-status
    """

    error = CodeSystemConcept(
        {
            "code": "error",
            "definition": "The resource was created in error, and should not be treated as valid (note: in many cases, for various data integrity related reasons, the information cannot be removed from the record)",
            "display": "error",
        }
    )
    """
    error

    The resource was created in error, and should not be treated as valid (note: in many cases, for various data integrity related reasons, the information cannot be removed from the record)
    """

    proposed = CodeSystemConcept(
        {
            "code": "proposed",
            "definition": "The resource describes an action or plan that is proposed, and not yet approved by the participants",
            "display": "proposed",
        }
    )
    """
    proposed

    The resource describes an action or plan that is proposed, and not yet approved by the participants
    """

    planned = CodeSystemConcept(
        {
            "code": "planned",
            "definition": "The resource describes a course of action that is planned and agreed/approved, but at the time of recording was still future",
            "display": "planned",
        }
    )
    """
    planned

    The resource describes a course of action that is planned and agreed/approved, but at the time of recording was still future
    """

    draft = CodeSystemConcept(
        {
            "code": "draft",
            "definition": "The information in the resource is still being prepared and edited",
            "display": "draft",
        }
    )
    """
    draft

    The information in the resource is still being prepared and edited
    """

    requested = CodeSystemConcept(
        {
            "code": "requested",
            "definition": "A fulfiller has been asked to perform this action, but it has not yet occurred",
            "display": "requested",
        }
    )
    """
    requested

    A fulfiller has been asked to perform this action, but it has not yet occurred
    """

    received = CodeSystemConcept(
        {
            "code": "received",
            "definition": "The fulfiller has received the request, but not yet agreed to carry out the action",
            "display": "received",
        }
    )
    """
    received

    The fulfiller has received the request, but not yet agreed to carry out the action
    """

    declined = CodeSystemConcept(
        {
            "code": "declined",
            "definition": "The fulfiller chose not to perform the action",
            "display": "declined",
        }
    )
    """
    declined

    The fulfiller chose not to perform the action
    """

    accepted = CodeSystemConcept(
        {
            "code": "accepted",
            "definition": "The fulfiller has decided to perform the action, and plans are in train to do this in the future",
            "display": "accepted",
        }
    )
    """
    accepted

    The fulfiller has decided to perform the action, and plans are in train to do this in the future
    """

    arrived = CodeSystemConcept(
        {
            "code": "arrived",
            "definition": "The pre-conditions for the action are all fulfilled, and it is imminent",
            "display": "arrived",
        }
    )
    """
    arrived

    The pre-conditions for the action are all fulfilled, and it is imminent
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "The resource describes information that is currently valid or a process that is presently occuring",
            "display": "active",
        }
    )
    """
    active

    The resource describes information that is currently valid or a process that is presently occuring
    """

    suspended = CodeSystemConcept(
        {
            "code": "suspended",
            "definition": "The process described/requested in this resource has been halted for some reason",
            "display": "suspended",
        }
    )
    """
    suspended

    The process described/requested in this resource has been halted for some reason
    """

    failed = CodeSystemConcept(
        {
            "code": "failed",
            "definition": "The process described/requested in the resource could not be completed, and no further action is planned",
            "display": "failed",
        }
    )
    """
    failed

    The process described/requested in the resource could not be completed, and no further action is planned
    """

    replaced = CodeSystemConcept(
        {
            "code": "replaced",
            "definition": "The information in this resource has been replaced by information in another resource",
            "display": "replaced",
        }
    )
    """
    replaced

    The information in this resource has been replaced by information in another resource
    """

    complete = CodeSystemConcept(
        {
            "code": "complete",
            "definition": "The process described/requested in the resource has been completed, and no further action is planned",
            "display": "complete",
        }
    )
    """
    complete

    The process described/requested in the resource has been completed, and no further action is planned
    """

    inactive = CodeSystemConcept(
        {
            "code": "inactive",
            "definition": "The resource describes information that is no longer valid or a process that is stopped occurring",
            "display": "inactive",
        }
    )
    """
    inactive

    The resource describes information that is no longer valid or a process that is stopped occurring
    """

    abandoned = CodeSystemConcept(
        {
            "code": "abandoned",
            "definition": "The process described/requested in the resource did not complete - usually due to some workflow error, and no further action is planned",
            "display": "abandoned",
        }
    )
    """
    abandoned

    The process described/requested in the resource did not complete - usually due to some workflow error, and no further action is planned
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "Authoring system does not know the status",
            "display": "unknown",
        }
    )
    """
    unknown

    Authoring system does not know the status
    """

    unconfirmed = CodeSystemConcept(
        {
            "code": "unconfirmed",
            "definition": "The information in this resource is not yet approved",
            "display": "unconfirmed",
        }
    )
    """
    unconfirmed

    The information in this resource is not yet approved
    """

    confirmed = CodeSystemConcept(
        {
            "code": "confirmed",
            "definition": "The information in this resource is approved",
            "display": "confirmed",
        }
    )
    """
    confirmed

    The information in this resource is approved
    """

    resolved = CodeSystemConcept(
        {
            "code": "resolved",
            "definition": "The issue identified by this resource is no longer of concern",
            "display": "resolved",
        }
    )
    """
    resolved

    The issue identified by this resource is no longer of concern
    """

    refuted = CodeSystemConcept(
        {
            "code": "refuted",
            "definition": "This information has been ruled out by testing and evaluation",
            "display": "refuted",
        }
    )
    """
    refuted

    This information has been ruled out by testing and evaluation
    """

    differential = CodeSystemConcept(
        {
            "code": "differential",
            "definition": "Potentially true?",
            "display": "differential",
        }
    )
    """
    differential

    Potentially true?
    """

    partial = CodeSystemConcept(
        {
            "code": "partial",
            "definition": "This information is still being assembled",
            "display": "partial",
        }
    )
    """
    partial

    This information is still being assembled
    """

    busy_unavailable = CodeSystemConcept(
        {
            "code": "busy-unavailable",
            "definition": "not available at this time/location",
            "display": "busy-unavailable",
        }
    )
    """
    busy-unavailable

    not available at this time/location
    """

    free = CodeSystemConcept(
        {"code": "free", "definition": "Free for scheduling", "display": "free"}
    )
    """
    free

    Free for scheduling
    """

    on_target = CodeSystemConcept(
        {"code": "on-target", "definition": "Ready to act", "display": "on-target"}
    )
    """
    on-target

    Ready to act
    """

    ahead_of_target = CodeSystemConcept(
        {
            "code": "ahead-of-target",
            "definition": "Ahead of the planned timelines",
            "display": "ahead-of-target",
        }
    )
    """
    ahead-of-target

    Ahead of the planned timelines
    """

    behind_target = CodeSystemConcept(
        {"code": "behind-target", "display": "behind-target"}
    )
    """
    behind-target

    
    """

    not_ready = CodeSystemConcept(
        {
            "code": "not-ready",
            "definition": "Behind the planned timelines",
            "display": "not-ready",
        }
    )
    """
    not-ready

    Behind the planned timelines
    """

    transduc_discon = CodeSystemConcept(
        {
            "code": "transduc-discon",
            "definition": "The device transducer is disconnected",
            "display": "transduc-discon",
        }
    )
    """
    transduc-discon

    The device transducer is disconnected
    """

    hw_discon = CodeSystemConcept(
        {
            "code": "hw-discon",
            "definition": "The hardware is disconnected",
            "display": "hw-discon",
        }
    )
    """
    hw-discon

    The hardware is disconnected
    """

    class Meta:
        resource = _resource
