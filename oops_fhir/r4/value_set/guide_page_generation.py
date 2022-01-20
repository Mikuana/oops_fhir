from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.guide_page_generation import (
    GuidePageGeneration as GuidePageGeneration_,
)


__all__ = ["GuidePageGeneration"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class GuidePageGeneration(GuidePageGeneration_):
    """
    GuidePageGeneration

    A code that indicates how the page is generated.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/guide-page-generation
    """

    class Meta:
        resource = _resource
