from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_reason import v3ActReason as v3ActReason_


__all__ = ["v3ActReason"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ActReason(v3ActReason_):
    """
    v3 Code System ActReason

     A set of codes specifying the motivation, cause, or rationale of an
Act, when such rationale is not reasonably represented as an
ActRelationship of type "has reason" linking to another Act.  Examples:
Example reasons that might qualify for being coded in this field might
be: "routine requirement", "infectious disease reporting requirement",
"on patient request", "required by law".

    Status: active - Version: 2018-08-12

    http://terminology.hl7.org/ValueSet/v3-ActReason
    """

    class Meta:
        resource = _resource
