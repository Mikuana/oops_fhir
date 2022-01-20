from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ResponseLevel"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ResponseLevel:
    """
    v3 Code System ResponseLevel

     Specifies whether a response is expected from the addressee of this
interaction and what level of detail that response should include

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ResponseLevel
    """

    c = CodeSystemConcept(
        {
            "code": "C",
            "definition": "Respond with exceptions and a notification of completion",
            "display": "completion",
        }
    )
    """
    completion

    Respond with exceptions and a notification of completion
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "Respond with exceptions, completion, modifications and include more detail information (if applicable)",
            "display": "detail",
        }
    )
    """
    detail

    Respond with exceptions, completion, modifications and include more detail information (if applicable)
    """

    e = CodeSystemConcept(
        {
            "code": "E",
            "definition": "Respond with exceptions only",
            "display": "exception",
        }
    )
    """
    exception

    Respond with exceptions only
    """

    f = CodeSystemConcept(
        {
            "code": "F",
            "definition": "Respond with exceptions, completion, and modification with detail (as above), and send positive confirmations even if no modifications are being made.",
            "display": "confirmation",
        }
    )
    """
    confirmation

    Respond with exceptions, completion, and modification with detail (as above), and send positive confirmations even if no modifications are being made.
    """

    n = CodeSystemConcept(
        {
            "code": "N",
            "definition": "Respond only with message level acknowledgements, i.e., only notify acceptance or rejection of the message, do not include any application-level detail",
            "display": "message-control",
        }
    )
    """
    message-control

    Respond only with message level acknowledgements, i.e., only notify acceptance or rejection of the message, do not include any application-level detail
    """

    r = CodeSystemConcept(
        {
            "code": "R",
            "definition": "Respond with exceptions, completions and modifications or revisions done before completion",
            "display": "modification",
        }
    )
    """
    modification

    Respond with exceptions, completions and modifications or revisions done before completion
    """

    x = CodeSystemConcept(
        {
            "code": "X",
            "definition": "Do not send any kind of response",
            "display": "none",
        }
    )
    """
    none

    Do not send any kind of response
    """

    class Meta:
        resource = _resource
