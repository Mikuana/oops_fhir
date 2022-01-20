from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_set_operator import v3SetOperator as v3SetOperator_


__all__ = ["v3SetOperator"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3SetOperator(v3SetOperator_):
    """
    v3 Code System SetOperator

    **** MISSING DEFINITIONS ****

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-SetOperator
    """

    class Meta:
        resource = _resource
