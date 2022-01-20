from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.substance_category_codes import (
    SubstanceCategoryCodes as SubstanceCategoryCodes_,
)


__all__ = ["SubstanceCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubstanceCategoryCodes(SubstanceCategoryCodes_):
    """
    Substance Category Codes

    Substance category codes

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/substance-category
    """

    class Meta:
        resource = _resource
