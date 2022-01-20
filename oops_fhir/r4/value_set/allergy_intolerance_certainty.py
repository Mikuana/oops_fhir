from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.allergy_intolerance_certainty import (
    AllergyIntoleranceCertainty as AllergyIntoleranceCertainty_,
)


__all__ = ["AllergyIntoleranceCertainty"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceCertainty(AllergyIntoleranceCertainty_):
    """
    AllergyIntoleranceCertainty

    Statement about the degree of clinical certainty that a specific
substance was the cause of the manifestation in a reaction event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reaction-event-certainty
    """

    class Meta:
        resource = _resource
