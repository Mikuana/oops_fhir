from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BiologicallyDerivedProductCategory"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BiologicallyDerivedProductCategory:
    """
    BiologicallyDerivedProductCategory

    Biologically Derived Product Category.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/product-category
    """

    organ = CodeSystemConcept(
        {
            "code": "organ",
            "definition": "A collection of tissues joined in a structural unit to serve a common function.",
            "display": "Organ",
        }
    )
    """
    Organ

    A collection of tissues joined in a structural unit to serve a common function.
    """

    tissue = CodeSystemConcept(
        {
            "code": "tissue",
            "definition": "An ensemble of similar cells and their extracellular matrix from the same origin that together carry out a specific function.",
            "display": "Tissue",
        }
    )
    """
    Tissue

    An ensemble of similar cells and their extracellular matrix from the same origin that together carry out a specific function.
    """

    fluid = CodeSystemConcept(
        {"code": "fluid", "definition": "Body fluid.", "display": "Fluid"}
    )
    """
    Fluid

    Body fluid.
    """

    cells = CodeSystemConcept(
        {"code": "cells", "definition": "Collection of cells.", "display": "Cells"}
    )
    """
    Cells

    Collection of cells.
    """

    biological_agent = CodeSystemConcept(
        {
            "code": "biologicalAgent",
            "definition": "Biological agent of unspecified type.",
            "display": "BiologicalAgent",
        }
    )
    """
    BiologicalAgent

    Biological agent of unspecified type.
    """

    class Meta:
        resource = _resource
