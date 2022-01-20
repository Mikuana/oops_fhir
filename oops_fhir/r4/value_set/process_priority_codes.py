from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.process_priority_codes import (
    ProcessPriorityCodes as ProcessPriorityCodes_,
)


__all__ = ["ProcessPriorityCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ProcessPriorityCodes(ProcessPriorityCodes_):
    """
    Process Priority Codes

    This value set includes the financial processing priority codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/process-priority
    """

    class Meta:
        resource = _resource
