from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["HGNC"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class HGNC(ValueSet):
    """
    H g n c

    HGNC: Human Gene Nomenclature Committee

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/genenames
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
