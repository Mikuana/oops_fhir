from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FinancialTaskInputTypeCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FinancialTaskInputTypeCodes:
    """
    Financial Task Input Type Codes

    This value set includes Financial Task Input Type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/financialtaskinputtype
    """

    include = CodeSystemConcept(
        {
            "code": "include",
            "definition": "The name of a resource to include in a selection.",
            "display": "Include",
        }
    )
    """
    Include

    The name of a resource to include in a selection.
    """

    exclude = CodeSystemConcept(
        {
            "code": "exclude",
            "definition": "The name of a resource to not include in a selection.",
            "display": "Exclude",
        }
    )
    """
    Exclude

    The name of a resource to not include in a selection.
    """

    origresponse = CodeSystemConcept(
        {
            "code": "origresponse",
            "definition": "A reference to the response resource to the original processing of a resource.",
            "display": "Original Response",
        }
    )
    """
    Original Response

    A reference to the response resource to the original processing of a resource.
    """

    reference = CodeSystemConcept(
        {
            "code": "reference",
            "definition": "A reference value which must be quoted to authorize an action.",
            "display": "Reference Number",
        }
    )
    """
    Reference Number

    A reference value which must be quoted to authorize an action.
    """

    item = CodeSystemConcept(
        {
            "code": "item",
            "definition": "The sequence number associated with an item for reprocessing.",
            "display": "Item Number",
        }
    )
    """
    Item Number

    The sequence number associated with an item for reprocessing.
    """

    period = CodeSystemConcept(
        {
            "code": "period",
            "definition": "The reference period for the action being requested.",
            "display": "Period",
        }
    )
    """
    Period

    The reference period for the action being requested.
    """

    status = CodeSystemConcept(
        {
            "code": "status",
            "definition": "The processing status from a check on the processing status of a resource such as the adjudication of a claim.",
            "display": "Status code",
        }
    )
    """
    Status code

    The processing status from a check on the processing status of a resource such as the adjudication of a claim.
    """

    class Meta:
        resource = _resource
