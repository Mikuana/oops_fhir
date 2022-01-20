from pathlib import Path

from fhir.resources.valueset import ValueSet as _ValueSet

from oops_fhir.utils import ValueSet


from oops_fhir.r4.code_system.audit_event_agent_network_type import (
    AuditEventAgentNetworkType as AuditEventAgentNetworkType_,
)


__all__ = ["AuditEventAgentNetworkType"]

_resource = _ValueSet.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventAgentNetworkType(AuditEventAgentNetworkType_):
    """
    AuditEventAgentNetworkType

    The type of network access point of this agent in the audit event.

    Status: draft - Version: 4.0.1

    http://hl7.org/fhir/ValueSet/network-type
    """

    class Meta:
        resource = _resource
