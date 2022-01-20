from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_orderable_drug_form import (
    v3orderableDrugForm as v3orderableDrugForm_,
)


__all__ = ["v3orderableDrugForm"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3orderableDrugForm(v3orderableDrugForm_):
    """
    v3 Code System orderableDrugForm

      OpenIssue:  Missing description.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-orderableDrugForm
    """

    class Meta:
        resource = _resource
