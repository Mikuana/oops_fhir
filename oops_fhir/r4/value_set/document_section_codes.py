from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DocumentSectionCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentSectionCodes(ValueSet):
    """
    Document Section Codes

    Document section codes (LOINC codes used in CCDA sections).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/doc-section-codes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
