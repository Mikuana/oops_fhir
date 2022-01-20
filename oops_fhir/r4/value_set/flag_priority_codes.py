from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.flag_priority_codes import (
    FlagPriorityCodes as FlagPriorityCodes_,
)


__all__ = ["FlagPriorityCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FlagPriorityCodes(FlagPriorityCodes_):
    """
    Flag Priority Codes

    This value set is provided as an exemplar. The value set is driven by
IHE Table B.8-4: Abnormal Flags, Alert Priority.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/flag-priority
    """

    class Meta:
        resource = _resource
