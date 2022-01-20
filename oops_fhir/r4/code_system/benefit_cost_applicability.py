from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["BenefitCostApplicability"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class BenefitCostApplicability:
    """
    Benefit cost applicability

    Whether the cost applies to in-network or out-of-network providers.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/applicability
    """

    in_network = CodeSystemConcept(
        {
            "code": "in-network",
            "definition": "Provider is contracted with the health insurance company to provide services to plan members for specific pre-negotiated rates",
            "display": "In Network",
        }
    )
    """
    In Network

    Provider is contracted with the health insurance company to provide services to plan members for specific pre-negotiated rates
    """

    out_of_network = CodeSystemConcept(
        {
            "code": "out-of-network",
            "definition": "Provider is  not contracted with the health insurance company to provide services to plan members for specific pre-negotiated rates",
            "display": "Out of Network",
        }
    )
    """
    Out of Network

    Provider is  not contracted with the health insurance company to provide services to plan members for specific pre-negotiated rates
    """

    other = CodeSystemConcept(
        {"code": "other", "definition": "Other applicability", "display": "Other"}
    )
    """
    Other

    Other applicability
    """

    class Meta:
        resource = _resource
