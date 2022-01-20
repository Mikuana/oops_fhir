from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["AllCPTcodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllCPTcodes(ValueSet):
    """
    All CPT codes

    A value set that includes all CPT codes

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/cpt-all
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
