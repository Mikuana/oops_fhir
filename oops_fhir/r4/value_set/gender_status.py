from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.gender_status import GenderStatus as GenderStatus_


__all__ = ["GenderStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GenderStatus(GenderStatus_):
    """
    Gender status

    This example value set defines a set of codes that can be used to
indicate the current state of the animal's reproductive organs.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/animal-genderstatus
    """

    class Meta:
        resource = _resource
