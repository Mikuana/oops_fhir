from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["TextureModifiedFoodTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TextureModifiedFoodTypeCodes(ValueSet):
    """
    Texture Modified Food Type Codes

    TextureModifiedFoodType: Codes for types of foods that are texture-
modified. This value set is composed SNOMED CT Concepts from SCTID
255620007 Foods (substance) and is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/modified-foodtype
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
