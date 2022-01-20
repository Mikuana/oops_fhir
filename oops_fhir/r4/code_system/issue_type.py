from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["IssueType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class IssueType:
    """
    IssueType

    A code that describes the type of issue.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/issue-type
    """

    invalid = CodeSystemConcept(
        {
            "code": "invalid",
            "concept": [
                {
                    "code": "structure",
                    "definition": "A structural issue in the content such as wrong namespace, unable to parse the content completely, invalid syntax, etc.",
                    "display": "Structural Issue",
                },
                {
                    "code": "required",
                    "definition": "A required element is missing.",
                    "display": "Required element missing",
                },
                {
                    "code": "value",
                    "definition": "An element or header value is invalid.",
                    "display": "Element value invalid",
                },
                {
                    "code": "invariant",
                    "definition": "A content validation rule failed - e.g. a schematron rule.",
                    "display": "Validation rule failed",
                },
            ],
            "definition": "Content invalid against the specification or a profile.",
            "display": "Invalid Content",
        }
    )
    """
    Invalid Content

    Content invalid against the specification or a profile.
    """

    security = CodeSystemConcept(
        {
            "code": "security",
            "concept": [
                {
                    "code": "login",
                    "definition": "The client needs to initiate an authentication process.",
                    "display": "Login Required",
                },
                {
                    "code": "unknown",
                    "definition": "The user or system was not able to be authenticated (either there is no process, or the proferred token is unacceptable).",
                    "display": "Unknown User",
                },
                {
                    "code": "expired",
                    "definition": "User session expired; a login may be required.",
                    "display": "Session Expired",
                },
                {
                    "code": "forbidden",
                    "definition": "The user does not have the rights to perform this action.",
                    "display": "Forbidden",
                },
                {
                    "code": "suppressed",
                    "definition": "Some information was not or might not have been returned due to business rules, consent or privacy rules, or access permission constraints.  This information may be accessible through alternate processes.",
                    "display": "Information  Suppressed",
                },
            ],
            "definition": "An authentication/authorization/permissions issue of some kind.",
            "display": "Security Problem",
        }
    )
    """
    Security Problem

    An authentication/authorization/permissions issue of some kind.
    """

    processing = CodeSystemConcept(
        {
            "code": "processing",
            "concept": [
                {
                    "code": "not-supported",
                    "definition": "The interaction, operation, resource or profile is not supported.",
                    "display": "Content not supported",
                },
                {
                    "code": "duplicate",
                    "definition": "An attempt was made to create a duplicate record.",
                    "display": "Duplicate",
                },
                {
                    "code": "multiple-matches",
                    "definition": "Multiple matching records were found when the operation required only one match.",
                    "display": "Multiple Matches",
                },
                {
                    "code": "not-found",
                    "concept": [
                        {
                            "code": "deleted",
                            "definition": "The reference pointed to content (usually a resource) that has been deleted.",
                            "display": "Deleted",
                        }
                    ],
                    "definition": "The reference provided was not found. In a pure RESTful environment, this would be an HTTP 404 error, but this code may be used where the content is not found further into the application architecture.",
                    "display": "Not Found",
                },
                {
                    "code": "too-long",
                    "definition": "Provided content is too long (typically, this is a denial of service protection type of error).",
                    "display": "Content Too Long",
                },
                {
                    "code": "code-invalid",
                    "definition": "The code or system could not be understood, or it was not valid in the context of a particular ValueSet.code.",
                    "display": "Invalid Code",
                },
                {
                    "code": "extension",
                    "definition": "An extension was found that was not acceptable, could not be resolved, or a modifierExtension was not recognized.",
                    "display": "Unacceptable Extension",
                },
                {
                    "code": "too-costly",
                    "definition": "The operation was stopped to protect server resources; e.g. a request for a value set expansion on all of SNOMED CT.",
                    "display": "Operation Too Costly",
                },
                {
                    "code": "business-rule",
                    "definition": "The content/operation failed to pass some business rule and so could not proceed.",
                    "display": "Business Rule Violation",
                },
                {
                    "code": "conflict",
                    "definition": "Content could not be accepted because of an edit conflict (i.e. version aware updates). (In a pure RESTful environment, this would be an HTTP 409 error, but this code may be used where the conflict is discovered further into the application architecture.).",
                    "display": "Edit Version Conflict",
                },
            ],
            "definition": "Processing issues. These are expected to be final e.g. there is no point resubmitting the same content unchanged.",
            "display": "Processing Failure",
        }
    )
    """
    Processing Failure

    Processing issues. These are expected to be final e.g. there is no point resubmitting the same content unchanged.
    """

    transient = CodeSystemConcept(
        {
            "code": "transient",
            "concept": [
                {
                    "code": "lock-error",
                    "definition": "A resource/record locking failure (usually in an underlying database).",
                    "display": "Lock Error",
                },
                {
                    "code": "no-store",
                    "definition": "The persistent store is unavailable; e.g. the database is down for maintenance or similar action, and the interaction or operation cannot be processed.",
                    "display": "No Store Available",
                },
                {
                    "code": "exception",
                    "definition": "An unexpected internal error has occurred.",
                    "display": "Exception",
                },
                {
                    "code": "timeout",
                    "definition": "An internal timeout has occurred.",
                    "display": "Timeout",
                },
                {
                    "code": "incomplete",
                    "definition": "Not all data sources typically accessed could be reached or responded in time, so the returned information might not be complete (applies to search interactions and some operations).",
                    "display": "Incomplete Results",
                },
                {
                    "code": "throttled",
                    "definition": "The system is not prepared to handle this request due to load management.",
                    "display": "Throttled",
                },
            ],
            "definition": "Transient processing issues. The system receiving the message may be able to resubmit the same content once an underlying issue is resolved.",
            "display": "Transient Issue",
        }
    )
    """
    Transient Issue

    Transient processing issues. The system receiving the message may be able to resubmit the same content once an underlying issue is resolved.
    """

    informational = CodeSystemConcept(
        {
            "code": "informational",
            "definition": "A message unrelated to the processing success of the completed operation (examples of the latter include things like reminders of password expiry, system maintenance times, etc.).",
            "display": "Informational Note",
        }
    )
    """
    Informational Note

    A message unrelated to the processing success of the completed operation (examples of the latter include things like reminders of password expiry, system maintenance times, etc.).
    """

    class Meta:
        resource = _resource
