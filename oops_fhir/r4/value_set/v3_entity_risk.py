from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_entity_risk import v3EntityRisk as v3EntityRisk_


__all__ = ["v3EntityRisk"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3EntityRisk(v3EntityRisk_):
    """
    v3 Code System EntityRisk

     Kinds of risks associated with the handling of the material..

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-EntityRisk
    """

    class Meta:
        resource = _resource
