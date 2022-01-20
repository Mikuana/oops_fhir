from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_document_completion import (
    v3DocumentCompletion as v3DocumentCompletion_,
)


__all__ = ["v3DocumentCompletion"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3DocumentCompletion(v3DocumentCompletion_):
    """
    v3 Code System DocumentCompletion

     Identifies the current completion state of a clinical document.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-DocumentCompletion
    """

    class Meta:
        resource = _resource
