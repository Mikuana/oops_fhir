from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_context_conduction_style import (
    v3HL7ContextConductionStyle as v3HL7ContextConductionStyle_,
)


__all__ = ["v3HL7ContextConductionStyle"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3HL7ContextConductionStyle(v3HL7ContextConductionStyle_):
    """
    v3 Code System HL7ContextConductionStyle

    The styles of context conduction usable by relationships within a static
model derived from tyhe HL7 Reference Information Model.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-HL7ContextConductionStyle
    """

    class Meta:
        resource = _resource
