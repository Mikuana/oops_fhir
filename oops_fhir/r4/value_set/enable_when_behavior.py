from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.enable_when_behavior import (
    EnableWhenBehavior as EnableWhenBehavior_,
)


__all__ = ["EnableWhenBehavior"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class EnableWhenBehavior(EnableWhenBehavior_):
    """
    EnableWhenBehavior

    Controls how multiple enableWhen values are interpreted -  whether all
or any must be true.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/questionnaire-enable-behavior
    """

    class Meta:
        resource = _resource
