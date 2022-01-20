from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["status"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class status:
    """
    Status

    The validation status of the target

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/CodeSystem/status
    """

    attested = CodeSystemConcept(
        {"code": "attested", "definition": "***TODO***", "display": "Attested"}
    )
    """
    Attested

    ***TODO***
    """

    validated = CodeSystemConcept(
        {"code": "validated", "definition": "***TODO***", "display": "Validated"}
    )
    """
    Validated

    ***TODO***
    """

    in_process = CodeSystemConcept(
        {"code": "in-process", "definition": "***TODO***", "display": "In process"}
    )
    """
    In process

    ***TODO***
    """

    req_revalid = CodeSystemConcept(
        {
            "code": "req-revalid",
            "definition": "***TODO***",
            "display": "Requires revalidation",
        }
    )
    """
    Requires revalidation

    ***TODO***
    """

    val_fail = CodeSystemConcept(
        {"code": "val-fail", "definition": "***TODO***", "display": "Validation failed"}
    )
    """
    Validation failed

    ***TODO***
    """

    reval_fail = CodeSystemConcept(
        {
            "code": "reval-fail",
            "definition": "***TODO***",
            "display": "Re-Validation failed",
        }
    )
    """
    Re-Validation failed

    ***TODO***
    """

    class Meta:
        resource = _resource
