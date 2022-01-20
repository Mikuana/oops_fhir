from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["repositoryType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class repositoryType:
    """
    repositoryType

    Type for access of external URI.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/repository-type
    """

    directlink = CodeSystemConcept(
        {
            "code": "directlink",
            "definition": "When URL is clicked, the resource can be seen directly (by webpage or by download link format).",
            "display": "Click and see",
        }
    )
    """
    Click and see

    When URL is clicked, the resource can be seen directly (by webpage or by download link format).
    """

    openapi = CodeSystemConcept(
        {
            "code": "openapi",
            "definition": "When the API method (e.g. [base_url]/[parameter]) related with the URL of the website is executed, the resource can be seen directly (usually in JSON or XML format).",
            "display": "The URL is the RESTful or other kind of API that can access to the result.",
        }
    )
    """
    The URL is the RESTful or other kind of API that can access to the result.

    When the API method (e.g. [base_url]/[parameter]) related with the URL of the website is executed, the resource can be seen directly (usually in JSON or XML format).
    """

    login = CodeSystemConcept(
        {
            "code": "login",
            "definition": "When logged into the website, the resource can be seen.",
            "display": "Result cannot be access unless an account is logged in",
        }
    )
    """
    Result cannot be access unless an account is logged in

    When logged into the website, the resource can be seen.
    """

    oauth = CodeSystemConcept(
        {
            "code": "oauth",
            "definition": "When logged in and  follow the API in the website related with URL, the resource can be seen.",
            "display": "Result need to be fetched with API and need LOGIN( or cookies are required when visiting the link of resource)",
        }
    )
    """
    Result need to be fetched with API and need LOGIN( or cookies are required when visiting the link of resource)

    When logged in and  follow the API in the website related with URL, the resource can be seen.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "Some other complicated or particular way to get resource from URL.",
            "display": "Some other complicated or particular way to get resource from URL.",
        }
    )
    """
    Some other complicated or particular way to get resource from URL.

    Some other complicated or particular way to get resource from URL.
    """

    class Meta:
        resource = _resource
