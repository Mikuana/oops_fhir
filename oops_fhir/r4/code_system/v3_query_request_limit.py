from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3QueryRequestLimit"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3QueryRequestLimit:
    """
    v3 Code System QueryRequestLimit

      Definition:  Defines the units associated with the magnitude of the
maximum size limit of a query response that can be accepted by the
requesting application.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-QueryRequestLimit
    """

    underscore_query_request_limit = CodeSystemConcept(
        {
            "code": "_QueryRequestLimit",
            "concept": [
                {
                    "code": "RD",
                    "definition": "Definition: The number of matching instances (number of focal classes). The document header class is the focal class of a document, a record would therefore be equal to a document.",
                    "display": "record",
                }
            ],
            "definition": "Definition: The number of matching instances (number of focal classes). The document header class is the focal class of a document, a record would therefore be equal to a document.",
            "display": "QueryRequestLimit",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    QueryRequestLimit

    Definition: The number of matching instances (number of focal classes). The document header class is the focal class of a document, a record would therefore be equal to a document.
    """

    class Meta:
        resource = _resource
