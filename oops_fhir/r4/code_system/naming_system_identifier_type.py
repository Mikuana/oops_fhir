from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["NamingSystemIdentifierType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class NamingSystemIdentifierType:
    """
    NamingSystemIdentifierType

    Identifies the style of unique identifier used to identify a namespace.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/namingsystem-identifier-type
    """

    oid = CodeSystemConcept(
        {
            "code": "oid",
            "definition": "An ISO object identifier; e.g. 1.2.3.4.5.",
            "display": "OID",
        }
    )
    """
    OID

    An ISO object identifier; e.g. 1.2.3.4.5.
    """

    uuid = CodeSystemConcept(
        {
            "code": "uuid",
            "definition": "A universally unique identifier of the form a5afddf4-e880-459b-876e-e4591b0acc11.",
            "display": "UUID",
        }
    )
    """
    UUID

    A universally unique identifier of the form a5afddf4-e880-459b-876e-e4591b0acc11.
    """

    uri = CodeSystemConcept(
        {
            "code": "uri",
            "definition": "A uniform resource identifier (ideally a URL - uniform resource locator); e.g. http://unitsofmeasure.org.",
            "display": "URI",
        }
    )
    """
    URI

    A uniform resource identifier (ideally a URL - uniform resource locator); e.g. http://unitsofmeasure.org.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "Some other type of unique identifier; e.g. HL7-assigned reserved string such as LN for LOINC.",
            "display": "Other",
        }
    )
    """
    Other

    Some other type of unique identifier; e.g. HL7-assigned reserved string such as LN for LOINC.
    """

    class Meta:
        resource = _resource
