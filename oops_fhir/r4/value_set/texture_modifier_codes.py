from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["TextureModifierCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class TextureModifierCodes(ValueSet):
    """
    Texture Modifier Codes

    TextureModifier: Codes for food consistency types or texture
modifications to apply to foods. This value set is composed of SNOMED CT
(US Extension and Core) Concepts from SCTID 229961002 Food consistency
types (substance) hierarchy and is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/texture-code
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
