from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.observation_category_codes import (
    ObservationCategoryCodes as ObservationCategoryCodes_,
)


__all__ = ["ObservationCategoryCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ObservationCategoryCodes(ObservationCategoryCodes_):
    """
    Observation Category Codes

    Codes to denote a guideline or policy statement.when a genetic test
result is being shared as a secondary finding.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/secondary-finding
    """

    class Meta:
        resource = _resource
