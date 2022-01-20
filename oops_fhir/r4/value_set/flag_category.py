from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.flag_category import FlagCategory as FlagCategory_


__all__ = ["FlagCategory"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FlagCategory(FlagCategory_):
    """
    Flag Category

    Example list of general categories for flagged issues. (Not complete or
necessarily appropriate.)

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/flag-category
    """

    class Meta:
        resource = _resource
