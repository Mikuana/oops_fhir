from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_document_storage import (
    v3DocumentStorage as v3DocumentStorage_,
)


__all__ = ["v3DocumentStorage"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3DocumentStorage(v3DocumentStorage_):
    """
    v3 Code System DocumentStorage

     Identifies the storage status of a document.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-DocumentStorage
    """

    class Meta:
        resource = _resource
