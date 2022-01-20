from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3DocumentSectionType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3DocumentSectionType(ValueSet):
    """
    V3 Value SetDocumentSectionType

     The type of document section.  Possible values: review of systems,
medical history, family history, microscopic findings, etc.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-DocumentSectionType
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
