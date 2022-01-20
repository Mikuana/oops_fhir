from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["FocalSubjectCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class FocalSubjectCodes(ValueSet):
    """
    Focal Subject Codes

    Example value set composed from SNOMED CT and HL7 V3 codes for
observation targets such as donor, fetus or spouse. As use cases are
discovered, more values may be added.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/focal-subject
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
