from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.v3_act_code import v3ActCode


__all__ = ["v3ObligationPolicy"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class v3ObligationPolicy(v3ActCode):
    """
    V3 Value SetObligationPolicy

     Conveys the mandated workflow action that an information custodian,
receiver, or user must perform.  Examples:    encrypt  Usage Note:  Per
OASIS XACML, an obligation is an operation specified in a policy or
policy that is performed in conjunction with the enforcement of an
access control decision.

    Status: active - Version: 2014-03-26

    http://terminology.hl7.org/ValueSet/v3-ObligationPolicy
    """

    class Meta:
        resource = _resource
