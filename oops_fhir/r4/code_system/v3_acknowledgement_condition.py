from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3AcknowledgementCondition"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3AcknowledgementCondition:
    """
    v3 Code System AcknowledgementCondition

     The codes identify the conditions under which accept acknowledgements
are required to be returned in response to this message. Note that
accept acknowledgement address two different issues at the same time:
reliable transport as well as syntactical correctness

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-AcknowledgementCondition
    """

    al = CodeSystemConcept(
        {
            "code": "AL",
            "definition": "Always send an acknowledgement.",
            "display": "Always",
        }
    )
    """
    Always

    Always send an acknowledgement.
    """

    er = CodeSystemConcept(
        {
            "code": "ER",
            "definition": "Send an acknowledgement for error/reject conditions only.",
            "display": "Error/reject only",
        }
    )
    """
    Error/reject only

    Send an acknowledgement for error/reject conditions only.
    """

    ne = CodeSystemConcept(
        {
            "code": "NE",
            "definition": "Never send an acknowledgement.",
            "display": "Never",
        }
    )
    """
    Never

    Never send an acknowledgement.
    """

    su = CodeSystemConcept(
        {
            "code": "SU",
            "definition": "Send an acknowledgement for successful completions only.",
            "display": "Successful only",
            "property": [{"code": "status", "valueCode": "retired"}],
        }
    )
    """
    Successful only

    Send an acknowledgement for successful completions only.
    """

    class Meta:
        resource = _resource
