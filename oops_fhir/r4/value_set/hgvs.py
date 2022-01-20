from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["HGVS"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class HGVS(ValueSet):
    """
    H g v s

    HGVS : Human Genome Variation Society

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/variants
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
