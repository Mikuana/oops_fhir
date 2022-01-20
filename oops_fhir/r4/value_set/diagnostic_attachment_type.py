from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.snomed_ct import SNOMEDCT


__all__ = ["DiagnosticAttachmentType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class DiagnosticAttachmentType(ValueSet):
    """
    Diagnostic attachment type

    Diagnostic Attachment Type codes from [SNOMED
CT](http://snomed.info/sct) where concept is-a 182836005 (Review of
medication (procedure)) or is-a 404684003 (Clinical finding (finding))

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/diagnostic-based-on-snomed
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
