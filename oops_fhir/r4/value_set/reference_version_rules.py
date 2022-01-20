from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.reference_version_rules import (
    ReferenceVersionRules as ReferenceVersionRules_,
)


__all__ = ["ReferenceVersionRules"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ReferenceVersionRules(ReferenceVersionRules_):
    """
    ReferenceVersionRules

    Whether a reference needs to be version specific or version independent,
or whether either can be used.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/reference-version-rules
    """

    class Meta:
        resource = _resource
