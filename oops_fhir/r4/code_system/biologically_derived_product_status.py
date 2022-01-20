from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BiologicallyDerivedProductStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BiologicallyDerivedProductStatus:
    """
    BiologicallyDerivedProductStatus

    Biologically Derived Product Status.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/product-status
    """

    available = CodeSystemConcept(
        {
            "code": "available",
            "definition": "Product is currently available for use.",
            "display": "Available",
        }
    )
    """
    Available

    Product is currently available for use.
    """

    unavailable = CodeSystemConcept(
        {
            "code": "unavailable",
            "definition": "Product is not currently available for use.",
            "display": "Unavailable",
        }
    )
    """
    Unavailable

    Product is not currently available for use.
    """

    class Meta:
        resource = _resource
