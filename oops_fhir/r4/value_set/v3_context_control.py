from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_context_control import (
    v3ContextControl as v3ContextControl_,
)


__all__ = ["v3ContextControl"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ContextControl(v3ContextControl_):
    """
    v3 Code System ContextControl

     A code that specifies how an ActRelationship or Participation
contributes to the context of an Act, and whether it may be propagated
to descendent Acts whose association allows such propagation (see also
attributes Participation.contextControlCode,
ActRelationship.contextControlCode,
ActRelationship.contextConductionInd).

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ContextControl
    """

    class Meta:
        resource = _resource
