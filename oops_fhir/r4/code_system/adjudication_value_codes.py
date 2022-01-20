from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdjudicationValueCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdjudicationValueCodes:
    """
    Adjudication Value Codes

    This value set includes a smattering of Adjudication Value codes which
includes codes to indicate the amounts eligible under the plan, the
amount of benefit, copays etc.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/adjudication
    """

    submitted = CodeSystemConcept(
        {
            "code": "submitted",
            "definition": "The total submitted amount for the claim or group or line item.",
            "display": "Submitted Amount",
        }
    )
    """
    Submitted Amount

    The total submitted amount for the claim or group or line item.
    """

    copay = CodeSystemConcept(
        {"code": "copay", "definition": "Patient Co-Payment", "display": "CoPay"}
    )
    """
    CoPay

    Patient Co-Payment
    """

    eligible = CodeSystemConcept(
        {
            "code": "eligible",
            "definition": "Amount of the change which is considered for adjudication.",
            "display": "Eligible Amount",
        }
    )
    """
    Eligible Amount

    Amount of the change which is considered for adjudication.
    """

    deductible = CodeSystemConcept(
        {
            "code": "deductible",
            "definition": "Amount deducted from the eligible amount prior to adjudication.",
            "display": "Deductible",
        }
    )
    """
    Deductible

    Amount deducted from the eligible amount prior to adjudication.
    """

    unallocdeduct = CodeSystemConcept(
        {
            "code": "unallocdeduct",
            "definition": "The amount of deductible which could not allocated to other line items.",
            "display": "Unallocated Deductible",
        }
    )
    """
    Unallocated Deductible

    The amount of deductible which could not allocated to other line items.
    """

    eligpercent = CodeSystemConcept(
        {
            "code": "eligpercent",
            "definition": "Eligible Percentage.",
            "display": "Eligible %",
        }
    )
    """
    Eligible %

    Eligible Percentage.
    """

    tax = CodeSystemConcept(
        {"code": "tax", "definition": "The amount of tax.", "display": "Tax"}
    )
    """
    Tax

    The amount of tax.
    """

    benefit = CodeSystemConcept(
        {
            "code": "benefit",
            "definition": "Amount payable under the coverage",
            "display": "Benefit Amount",
        }
    )
    """
    Benefit Amount

    Amount payable under the coverage
    """

    class Meta:
        resource = _resource
