from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.diet import Diet as Diet_


__all__ = ["Diet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Diet(Diet_):
    """
    Diet

    This value set defines a set of codes that can be used to indicate
dietary preferences or restrictions a patient may have.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/encounter-diet
    """

    class Meta:
        resource = _resource
