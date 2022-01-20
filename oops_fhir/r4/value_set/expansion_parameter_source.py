from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.expansion_parameter_source import (
    ExpansionParameterSource as ExpansionParameterSource_,
)


__all__ = ["ExpansionParameterSource"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ExpansionParameterSource(ExpansionParameterSource_):
    """
    ExpansionParameterSource

    Declares what the source of a parameter is.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/expansion-parameter-source
    """

    class Meta:
        resource = _resource
