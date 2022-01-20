from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.allergy_intolerance_severity import (
    AllergyIntoleranceSeverity as AllergyIntoleranceSeverity_,
)


__all__ = ["AllergyIntoleranceSeverity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceSeverity(AllergyIntoleranceSeverity_):
    """
    AllergyIntoleranceSeverity

    Clinical assessment of the severity of a reaction event as a whole,
potentially considering multiple different manifestations.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reaction-event-severity
    """

    class Meta:
        resource = _resource
