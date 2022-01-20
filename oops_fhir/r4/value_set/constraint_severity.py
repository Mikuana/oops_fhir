from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.constraint_severity import (
    ConstraintSeverity as ConstraintSeverity_,
)


__all__ = ["ConstraintSeverity"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ConstraintSeverity(ConstraintSeverity_):
    """
    ConstraintSeverity

    SHALL applications comply with this constraint?

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/constraint-severity
    """

    class Meta:
        resource = _resource
