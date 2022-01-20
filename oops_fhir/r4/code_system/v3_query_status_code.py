from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3QueryStatusCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryStatusCode:
    """
    v3 Code System QueryStatusCode

     A code specifying the state of the Query.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-QueryStatusCode
    """

    aborted = CodeSystemConcept(
        {"code": "aborted", "definition": "Query status aborted", "display": "aborted"}
    )
    """
    aborted

    Query status aborted
    """

    delivered_response = CodeSystemConcept(
        {
            "code": "deliveredResponse",
            "definition": "Query Status delivered response",
            "display": "deliveredResponse",
        }
    )
    """
    deliveredResponse

    Query Status delivered response
    """

    executing = CodeSystemConcept(
        {
            "code": "executing",
            "definition": "Query Status executing",
            "display": "executing",
        }
    )
    """
    executing

    Query Status executing
    """

    new = CodeSystemConcept(
        {"code": "new", "definition": "Query Status new", "display": "new"}
    )
    """
    new

    Query Status new
    """

    wait_continued_query_response = CodeSystemConcept(
        {
            "code": "waitContinuedQueryResponse",
            "definition": "Query Status wait continued",
            "display": "waitContinuedQueryResponse",
        }
    )
    """
    waitContinuedQueryResponse

    Query Status wait continued
    """

    class Meta:
        resource = _resource
