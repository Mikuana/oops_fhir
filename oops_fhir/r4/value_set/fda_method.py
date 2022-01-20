from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FDAMethod"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FDAMethod(ValueSet):
    """
    F d a- method

    This value set includes sequence quality method

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/sequence-quality-method
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
