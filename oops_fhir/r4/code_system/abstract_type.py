from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AbstractType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AbstractType:
    """
    AbstractType

    A list of the base types defined by this version of the FHIR
specification - types that are defined, but for which only
specializations actually are created.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/abstract-types
    """

    type_ = CodeSystemConcept(
        {
            "code": "Type",
            "definition": "A place holder that means any kind of data type",
            "display": "Type",
        }
    )
    """
    Type

    A place holder that means any kind of data type
    """

    any_ = CodeSystemConcept(
        {
            "code": "Any",
            "definition": "A place holder that means any kind of resource",
            "display": "Any",
        }
    )
    """
    Any

    A place holder that means any kind of resource
    """

    class Meta:
        resource = _resource
