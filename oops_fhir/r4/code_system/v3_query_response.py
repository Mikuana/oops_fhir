from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3QueryResponse"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryResponse:
    """
    v3 Code System QueryResponse

     A code classifying the general nature of the response to a given query.
Includes whether or not data was found, or whether an error occurred.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-QueryResponse
    """

    ae = CodeSystemConcept(
        {
            "code": "AE",
            "definition": "Query Error.  Application Error.",
            "display": "ApplicationError",
        }
    )
    """
    ApplicationError

    Query Error.  Application Error.
    """

    nf = CodeSystemConcept(
        {
            "code": "NF",
            "definition": "No errors, but no data was found matching the query request specification.",
            "display": "No data found",
        }
    )
    """
    No data found

    No errors, but no data was found matching the query request specification.
    """

    ok = CodeSystemConcept(
        {
            "code": "OK",
            "definition": "Query reponse data found for 1 or more result sets matching the query request specification.",
            "display": "Data found",
        }
    )
    """
    Data found

    Query reponse data found for 1 or more result sets matching the query request specification.
    """

    qe = CodeSystemConcept(
        {
            "code": "QE",
            "definition": "QueryError. Problem with input ParmetersError",
            "display": "QueryParameterError",
        }
    )
    """
    QueryParameterError

    QueryError. Problem with input ParmetersError
    """

    class Meta:
        resource = _resource
