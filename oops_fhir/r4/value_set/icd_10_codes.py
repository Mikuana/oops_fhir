from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ICD10Codes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ICD10Codes(ValueSet):
    """
    ICD-10 Codes

    This value set includes sample ICD-10 codes.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/icd-10
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
