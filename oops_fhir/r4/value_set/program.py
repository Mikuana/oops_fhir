from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.program import Program as Program_


__all__ = ["Program"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class Program(Program_):
    """
    Program

    This value set defines an example set of codes that could be can be used
to classify groupings of service-types/specialties.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/program
    """

    class Meta:
        resource = _resource
