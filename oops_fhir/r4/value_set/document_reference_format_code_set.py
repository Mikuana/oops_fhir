from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DocumentReferenceFormatCodeSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentReferenceFormatCodeSet(ValueSet):
    """
    DocumentReference Format Code Set

    The value set is defined to be the set of format codes defined by the
IHE Technical Framework, and also including additional format codes
defined by the    HL7. The value set is listed in HITSP C80 Table 2-153
Format Code Value Set Definition,    with additions published later by
IHE as published    at
http://wiki.ihe.net/index.php?title=IHE_Format_Codes   and with
additions published later by HL7 as published at
https://confluence.hl7.org/display/SD/Format+Codes+for+IHE+XDS.   This
is the code specifying the technical format of the document. Along with
the typeCode,    it should provide sufficient information to allow any
potential document consumer to know    if it will be able to process the
document. The code shall be sufficiently specific to    ensure
processing/display by identifying a document encoding, structure and
template. The actual list of codes here is incomplete

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/formatcodes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
