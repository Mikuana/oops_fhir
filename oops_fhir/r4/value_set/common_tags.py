from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.common_tags import CommonTags as CommonTags_


__all__ = ["CommonTags"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class CommonTags(CommonTags_):
    """
    Common Tags

    Common Tag Codes defined by FHIR project

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/common-tags
    """

    class Meta:
        resource = _resource
