from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ResponseMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ResponseMode:
    """
    v3 Code System ResponseMode

     Specifies the mode, immediate versus deferred or queued, by which a
receiver should communicate its receiver responsibilities.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ResponseMode
    """

    d = CodeSystemConcept(
        {
            "code": "D",
            "definition": "The receiver may respond in a non-immediate manner. Note: this will be the default value.",
            "display": "deferred",
        }
    )
    """
    deferred

    The receiver may respond in a non-immediate manner. Note: this will be the default value.
    """

    i = CodeSystemConcept(
        {
            "code": "I",
            "definition": "The receiver is required to assume that the sender is blocking and behave appropriately by sending an immediate response.",
            "display": "immediate",
        }
    )
    """
    immediate

    The receiver is required to assume that the sender is blocking and behave appropriately by sending an immediate response.
    """

    q = CodeSystemConcept(
        {
            "code": "Q",
            "definition": "The receiver shall keep any application responses in a queue until such time as the queue is polled.",
            "display": "queue",
        }
    )
    """
    queue

    The receiver shall keep any application responses in a queue until such time as the queue is polled.
    """

    class Meta:
        resource = _resource
