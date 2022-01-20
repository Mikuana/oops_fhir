from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["v3xBasicConfidentialityKind"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3xBasicConfidentialityKind(ValueSet):
    """
    V3 Value Setx_BasicConfidentialityKind

      Description:  Used to enumerate the typical confidentiality
constraints placed upon a clinical document.  Usage Note:
x_BasicConfidentialityKind is a subset of Confidentiality codes that are
used as metadata indicating the receiver responsibility to comply with
normally applicable jurisdictional privacy law or disclosure
authorization; that the receiver may not disclose this information
except as directed by the information custodian, who may be the
information subject; or that the receiver may not disclose this
information except as directed by the information custodian, who may be
the information subject.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-xBasicConfidentialityKind
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
