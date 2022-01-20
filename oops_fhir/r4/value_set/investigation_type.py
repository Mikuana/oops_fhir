from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["InvestigationType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class InvestigationType(ValueSet):
    """
    Investigation Type

    Example value set for investigation type.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/investigation-sets
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
