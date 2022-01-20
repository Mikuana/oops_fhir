from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_v3_conformance import (
    v3hl7V3Conformance as v3hl7V3Conformance_,
)


__all__ = ["v3hl7V3Conformance"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7V3Conformance(v3hl7V3Conformance_):
    """
    v3 Code System hl7V3Conformance

      Description:  Identifies allowed codes for HL7aTMs v3 conformance
property.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7V3Conformance
    """

    class Meta:
        resource = _resource
