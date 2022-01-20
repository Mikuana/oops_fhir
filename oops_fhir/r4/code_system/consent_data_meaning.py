from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConsentDataMeaning"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConsentDataMeaning:
    """
    ConsentDataMeaning

    How a resource reference is interpreted when testing consent
restrictions.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/consent-data-meaning
    """

    instance = CodeSystemConcept(
        {
            "code": "instance",
            "definition": "The consent applies directly to the instance of the resource.",
            "display": "Instance",
        }
    )
    """
    Instance

    The consent applies directly to the instance of the resource.
    """

    related = CodeSystemConcept(
        {
            "code": "related",
            "definition": "The consent applies directly to the instance of the resource and instances it refers to.",
            "display": "Related",
        }
    )
    """
    Related

    The consent applies directly to the instance of the resource and instances it refers to.
    """

    dependents = CodeSystemConcept(
        {
            "code": "dependents",
            "definition": "The consent applies directly to the instance of the resource and instances that refer to it.",
            "display": "Dependents",
        }
    )
    """
    Dependents

    The consent applies directly to the instance of the resource and instances that refer to it.
    """

    authoredby = CodeSystemConcept(
        {
            "code": "authoredby",
            "definition": "The consent applies to instances of resources that are authored by.",
            "display": "AuthoredBy",
        }
    )
    """
    AuthoredBy

    The consent applies to instances of resources that are authored by.
    """

    class Meta:
        resource = _resource
