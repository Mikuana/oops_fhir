from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ExpressionLanguage"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ExpressionLanguage:
    """
    ExpressionLanguage

    The media type of the expression language.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/expression-language
    """

    text_cql = CodeSystemConcept(
        {
            "code": "text/cql",
            "definition": "Clinical Quality Language.",
            "display": "CQL",
        }
    )
    """
    CQL

    Clinical Quality Language.
    """

    text_fhirpath = CodeSystemConcept(
        {"code": "text/fhirpath", "definition": "FHIRPath.", "display": "FHIRPath"}
    )
    """
    FHIRPath

    FHIRPath.
    """

    application_x_fhir_query = CodeSystemConcept(
        {
            "code": "application/x-fhir-query",
            "definition": "FHIR's RESTful query syntax - typically independent of base URL.",
            "display": "FHIR Query",
        }
    )
    """
    FHIR Query

    FHIR's RESTful query syntax - typically independent of base URL.
    """

    class Meta:
        resource = _resource
