from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.allergy_intolerance_substance_exposure_risk import (
    AllergyIntoleranceSubstanceExposureRisk as AllergyIntoleranceSubstanceExposureRisk_,
)


__all__ = ["AllergyIntoleranceSubstanceExposureRisk"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceSubstanceExposureRisk(AllergyIntoleranceSubstanceExposureRisk_):
    """
    AllergyIntoleranceSubstanceExposureRisk

    The risk of an adverse reaction (allergy or intolerance) for this
patient upon exposure to the substance (including pharmaceutical
products).

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/allerg-intol-substance-exp-risk
    """

    class Meta:
        resource = _resource
