from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FHIRDocumentTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FHIRDocumentTypeCodes(ValueSet):
    """
    FHIR Document Type Codes

    FHIR Document Codes - all LOINC codes where scale type = 'DOC'.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/doc-typecodes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
