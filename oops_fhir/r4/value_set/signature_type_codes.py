from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.signature_type_codes import (
    SignatureTypeCodes as SignatureTypeCodes_,
)


__all__ = ["SignatureTypeCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class SignatureTypeCodes(SignatureTypeCodes_):
    """
    Signature Type Codes

    The Digital Signature Purposes, an indication of the reason an entity
signs a document. This is included in the signed information and can be
used when determining accountability for various actions concerning the
document. Examples include: author, transcriptionist/recorder, and
witness.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/signature-type
    """

    class Meta:
        resource = _resource
