from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_tribal_entity_us import (
    v3TribalEntityUS as v3TribalEntityUS_,
)


__all__ = ["v3TribalEntityUS"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3TribalEntityUS(v3TribalEntityUS_):
    """
    v3 Code System TribalEntityUS

     INDIAN ENTITIES RECOGNIZED AND ELIGIBLE TO RECEIVE SERVICES FROM THE
UNITED STATES BUREAU OF INDIAN AFFAIRS

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-TribalEntityUS
    """

    class Meta:
        resource = _resource
