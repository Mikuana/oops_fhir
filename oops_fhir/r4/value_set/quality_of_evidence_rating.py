from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.quality_of_evidence_rating import (
    QualityOfEvidenceRating as QualityOfEvidenceRating_,
)


__all__ = ["QualityOfEvidenceRating"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class QualityOfEvidenceRating(QualityOfEvidenceRating_):
    """
    QualityOfEvidenceRating

    A rating system that describes the quality of evidence such as the
GRADE, DynaMed, or Oxford CEBM systems.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/evidence-quality
    """

    class Meta:
        resource = _resource
