from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DocumentTypeValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentTypeValueSet(ValueSet):
    """
    Document Type Value Set

    This is the code specifying the precise type of document (e.g. Pulmonary
History and  Physical, Discharge Summary, Ultrasound Report, etc.). The
Document Type value set includes all LOINC  values listed in HITSP C80
Table 2-144 Document Class Value Set Definition above used for Document
Class,  and all LOINC values whose SCALE is DOC in the LOINC database.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/c80-doc-typecodes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
