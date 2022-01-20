from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["MimeTypes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class MimeTypes(ValueSet):
    """
    MimeType

    This value set includes all possible codes from BCP-13
(http://tools.ietf.org/html/bcp13)

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/mimetypes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
