from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_relational_operator import (
    v3RelationalOperator as v3RelationalOperator_,
)


__all__ = ["v3RelationalOperator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3RelationalOperator(v3RelationalOperator_):
    """
    v3 Code System RelationalOperator

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-RelationalOperator
    """

    class Meta:
        resource = _resource
