from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SupplyDeliveryStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SupplyDeliveryStatus:
    """
    SupplyDeliveryStatus

    Status of the supply delivery.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/supplydelivery-status
    """

    in_progress = CodeSystemConcept(
        {
            "code": "in-progress",
            "definition": "Supply has been requested, but not delivered.",
            "display": "In Progress",
        }
    )
    """
    In Progress

    Supply has been requested, but not delivered.
    """

    completed = CodeSystemConcept(
        {
            "code": "completed",
            "definition": 'Supply has been delivered ("completed").',
            "display": "Delivered",
        }
    )
    """
    Delivered

    Supply has been delivered ("completed").
    """

    abandoned = CodeSystemConcept(
        {
            "code": "abandoned",
            "definition": "Delivery was not completed.",
            "display": "Abandoned",
        }
    )
    """
    Abandoned

    Delivery was not completed.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": 'This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "abandoned" rather than "entered-in-error".).',
            "display": "Entered In Error",
        }
    )
    """
    Entered In Error

    This electronic record should never have existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred, the status should be "abandoned" rather than "entered-in-error".).
    """

    class Meta:
        resource = _resource
