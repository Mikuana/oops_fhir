from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_priority import v3ActPriority as v3ActPriority_


__all__ = ["v3ActPriority"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActPriority(v3ActPriority_):
    """
    v3 Code System ActPriority

     A set of codes (e.g., for routine, emergency), specifying the urgency
under which the Act happened, can happen, is happening, is intended to
happen, or is requested/demanded to happen.

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActPriority
    """

    class Meta:
        resource = _resource
