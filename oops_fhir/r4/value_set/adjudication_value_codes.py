from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.adjudication_value_codes import (
    AdjudicationValueCodes as AdjudicationValueCodes_,
)


__all__ = ["AdjudicationValueCodes"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AdjudicationValueCodes(AdjudicationValueCodes_):
    """
    Adjudication Value Codes

    This value set includes a smattering of Adjudication Value codes which
includes codes to indicate the amounts eligible under the plan, the
amount of benefit, copays etc.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/adjudication
    """

    class Meta:
        resource = _resource
