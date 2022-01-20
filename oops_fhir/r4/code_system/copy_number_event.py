from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["CopyNumberEvent"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class CopyNumberEvent:
    """
    CopyNumberEvent

    Copy Number Event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/copy-number-event
    """

    amp = CodeSystemConcept(
        {"code": "amp", "definition": "amplification.", "display": "amplification"}
    )
    """
    amplification

    amplification.
    """

    del_ = CodeSystemConcept(
        {"code": "del", "definition": "deletion.", "display": "deletion"}
    )
    """
    deletion

    deletion.
    """

    lof = CodeSystemConcept(
        {
            "code": "lof",
            "definition": "loss of function.",
            "display": "loss of function",
        }
    )
    """
    loss of function

    loss of function.
    """

    class Meta:
        resource = _resource
