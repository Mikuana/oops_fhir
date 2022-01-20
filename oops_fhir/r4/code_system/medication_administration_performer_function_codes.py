from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["MedicationAdministrationPerformerFunctionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class MedicationAdministrationPerformerFunctionCodes:
    """
    Medication administration  performer  function  codes

    MedicationAdministration Performer Function Codes

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/med-admin-perform-function
    """

    performer = CodeSystemConcept(
        {
            "code": "performer",
            "definition": "A person, non-person living subject, organization or device that who actually and principally carries out the action",
            "display": "Performer",
        }
    )
    """
    Performer

    A person, non-person living subject, organization or device that who actually and principally carries out the action
    """

    verifier = CodeSystemConcept(
        {
            "code": "verifier",
            "definition": "A person who verifies the correctness and appropriateness of the service (plan, order, event, etc.) and hence takes on accountability.",
            "display": "Verifier",
        }
    )
    """
    Verifier

    A person who verifies the correctness and appropriateness of the service (plan, order, event, etc.) and hence takes on accountability.
    """

    witness = CodeSystemConcept(
        {
            "code": "witness",
            "definition": "A person witnessing the action happening without doing anything. A witness is not necessarily aware, much less approves of anything stated in the service event. Example for a witness is students watching an operation or an advanced directive witness.",
            "display": "Witness",
        }
    )
    """
    Witness

    A person witnessing the action happening without doing anything. A witness is not necessarily aware, much less approves of anything stated in the service event. Example for a witness is students watching an operation or an advanced directive witness.
    """

    class Meta:
        resource = _resource
