from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["DocumentClassValueSet"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DocumentClassValueSet(ValueSet):
    """
    Document Class Value Set

    This is the code specifying the high-level kind of document (e.g.
Prescription, Discharge Summary, Report, etc.). Note: Class code for
documents comes from LOINC, and is based upon one of the following:The
type of service described by the document. It is described at a very
high level in Section 7.3 of the LOINC Manual. The type study performed.
It was determined by identifying modalities for study reports. The
section of the chart where the document is placed. It was determined
from the SETs created for Claims Attachment requests.

    Status: active - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/document-classcodes
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
