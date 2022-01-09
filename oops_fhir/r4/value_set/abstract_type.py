"""
AbstractType

A list of the base types defined by this version of the FHIR
specification - types that are defined, but for which only
specializations actually are created.

Status: active - Version: 4.0.1

http://hl7.org/fhir/ValueSet/abstract-types
"""
from pathlib import Path

from fhir.resources.valueset import ValueSet


from oops_fhir.r4.code_system.abstract_type import (
    v_type,
    v_any,
)


__all__ = ["v_type", "v_any"]

resource = ValueSet.parse_file(Path(__file__).with_suffix(".json"))
