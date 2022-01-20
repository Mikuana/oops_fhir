from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_container_cap import v3ContainerCap as v3ContainerCap_


__all__ = ["v3ContainerCap"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ContainerCap(v3ContainerCap_):
    """
    v3 Code System ContainerCap

     The type of cap associated with a container

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ContainerCap
    """

    class Meta:
        resource = _resource
