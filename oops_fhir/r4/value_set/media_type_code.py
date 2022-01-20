from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["MediaTypeCode"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MediaTypeCode(ValueSet):
    """
    Media Type Code

    Media Type Code

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/dicm-405-mediatype
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
