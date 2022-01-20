from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_hl7_cmetattribution import (
    v3hl7CMETAttribution as v3hl7CMETAttribution_,
)


__all__ = ["v3hl7CMETAttribution"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7CMETAttribution(v3hl7CMETAttribution_):
    """
    v3 Code System hl7CMETAttribution

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-hl7CMETAttribution
    """

    class Meta:
        resource = _resource
