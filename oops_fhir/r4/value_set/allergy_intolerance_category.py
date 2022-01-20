from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.allergy_intolerance_category import (
    AllergyIntoleranceCategory as AllergyIntoleranceCategory_,
)


__all__ = ["AllergyIntoleranceCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceCategory(AllergyIntoleranceCategory_):
    """
    AllergyIntoleranceCategory

    Category of an identified substance associated with allergies or
intolerances.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/allergy-intolerance-category
    """

    class Meta:
        resource = _resource
