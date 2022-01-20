from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ContainerMaterials"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ContainerMaterials(ValueSet):
    """
    Types of material for specimen containers

    This value set includes SNOMED CT codes for materials that specimen
containers are made of

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/container-material
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
