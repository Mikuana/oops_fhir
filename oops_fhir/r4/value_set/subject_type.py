from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["SubjectType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SubjectType(ValueSet):
    """
    Subject type

    Possible types of subjects.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/subject-type
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
