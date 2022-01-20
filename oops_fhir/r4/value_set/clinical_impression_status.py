from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


__all__ = ["ClinicalImpressionStatus"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class ClinicalImpressionStatus(ValueSet):
    """
    Clinical Impression Status

    Codes that reflect the current state of a clinical impression within its
overall lifecycle.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/clinicalimpression-status
    """

    # TODO: fix this template issue1
    pass

    class Meta:
        resource = _resource
