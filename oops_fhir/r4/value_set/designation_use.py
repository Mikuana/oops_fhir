from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DesignationUse"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DesignationUse(ValueSet):
    """
    Designation Use

    Details of how a designation would be used

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/designation-use
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
