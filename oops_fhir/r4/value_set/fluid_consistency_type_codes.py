from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FluidConsistencyTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FluidConsistencyTypeCodes(ValueSet):
    """
    Fluid Consistency Type Codes

    FluidConsistencyType :  Codes used to represent the consistency of
fluids and liquids provided to the patient. This value set includes
concepts from [SNOMED CT](http://snomed.info/sct)(US Extension) where
concept is a 435681000124103  (Dietary liquid consistency diet
(regime/therapy)). It is provided as a suggestive example.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/consistency-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
