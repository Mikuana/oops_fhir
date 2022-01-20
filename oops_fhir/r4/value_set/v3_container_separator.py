from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_container_separator import (
    v3ContainerSeparator as v3ContainerSeparator_,
)


__all__ = ["v3ContainerSeparator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ContainerSeparator(v3ContainerSeparator_):
    """
    v3 Code System ContainerSeparator

     A material in a blood collection container that facilites the
separation of of blood cells from serum or plasma

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ContainerSeparator
    """

    class Meta:
        resource = _resource
