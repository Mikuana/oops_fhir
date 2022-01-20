from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ChargeItemStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ChargeItemStatus:
    """
    ChargeItemStatus

    Codes identifying the lifecycle stage of a ChargeItem.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/chargeitem-status
    """

    planned = CodeSystemConcept(
        {
            "code": "planned",
            "definition": "The charge item has been entered, but the charged service is not  yet complete, so it shall not be billed yet but might be used in the context of pre-authorization.",
            "display": "Planned",
        }
    )
    """
    Planned

    The charge item has been entered, but the charged service is not  yet complete, so it shall not be billed yet but might be used in the context of pre-authorization.
    """

    billable = CodeSystemConcept(
        {
            "code": "billable",
            "definition": "The charge item is ready for billing.",
            "display": "Billable",
        }
    )
    """
    Billable

    The charge item is ready for billing.
    """

    not_billable = CodeSystemConcept(
        {
            "code": "not-billable",
            "definition": "The charge item has been determined to be not billable (e.g. due to rules associated with the billing code).",
            "display": "Not billable",
        }
    )
    """
    Not billable

    The charge item has been determined to be not billable (e.g. due to rules associated with the billing code).
    """

    aborted = CodeSystemConcept(
        {
            "code": "aborted",
            "definition": "The processing of the charge was aborted.",
            "display": "Aborted",
        }
    )
    """
    Aborted

    The processing of the charge was aborted.
    """

    billed = CodeSystemConcept(
        {
            "code": "billed",
            "definition": "The charge item has been billed (e.g. a billing engine has generated financial transactions by applying the associated ruled for the charge item to the context of the Encounter, and placed them into Claims/Invoices.",
            "display": "Billed",
        }
    )
    """
    Billed

    The charge item has been billed (e.g. a billing engine has generated financial transactions by applying the associated ruled for the charge item to the context of the Encounter, and placed them into Claims/Invoices.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The charge item has been entered in error and should not be processed for billing.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The charge item has been entered in error and should not be processed for billing.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": 'The authoring system does not know which of the status values currently applies for this charge item  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, it\'s just not known which one.',
            "display": "Unknown",
        }
    )
    """
    Unknown

    The authoring system does not know which of the status values currently applies for this charge item  Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known which one.
    """

    class Meta:
        resource = _resource
