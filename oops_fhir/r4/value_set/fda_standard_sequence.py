from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FDAStandardSequence"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FDAStandardSequence(ValueSet):
    """
    F d a- standard sequence

    This value set includes sequence quality standard

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/sequence-quality-standardSequence
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
