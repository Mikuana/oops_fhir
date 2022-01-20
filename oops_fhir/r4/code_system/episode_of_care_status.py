from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["EpisodeOfCareStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class EpisodeOfCareStatus:
    """
    EpisodeOfCareStatus

    The status of the episode of care.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/episode-of-care-status
    """

    planned = CodeSystemConcept(
        {
            "code": "planned",
            "definition": "This episode of care is planned to start at the date specified in the period.start. During this status, an organization may perform assessments to determine if the patient is eligible to receive services, or be organizing to make resources available to provide care services.",
            "display": "Planned",
        }
    )
    """
    Planned

    This episode of care is planned to start at the date specified in the period.start. During this status, an organization may perform assessments to determine if the patient is eligible to receive services, or be organizing to make resources available to provide care services.
    """

    waitlist = CodeSystemConcept(
        {
            "code": "waitlist",
            "definition": "This episode has been placed on a waitlist, pending the episode being made active (or cancelled).",
            "display": "Waitlist",
        }
    )
    """
    Waitlist

    This episode has been placed on a waitlist, pending the episode being made active (or cancelled).
    """

    active = CodeSystemConcept(
        {
            "code": "active",
            "definition": "This episode of care is current.",
            "display": "Active",
        }
    )
    """
    Active

    This episode of care is current.
    """

    onhold = CodeSystemConcept(
        {
            "code": "onhold",
            "definition": "This episode of care is on hold; the organization has limited responsibility for the patient (such as while on respite).",
            "display": "On Hold",
        }
    )
    """
    On Hold

    This episode of care is on hold; the organization has limited responsibility for the patient (such as while on respite).
    """

    finished = CodeSystemConcept(
        {
            "code": "finished",
            "definition": 'This episode of care is finished and the organization is not expecting to be providing further care to the patient. Can also be known as "closed", "completed" or other similar terms.',
            "display": "Finished",
        }
    )
    """
    Finished

    This episode of care is finished and the organization is not expecting to be providing further care to the patient. Can also be known as "closed", "completed" or other similar terms.
    """

    cancelled = CodeSystemConcept(
        {
            "code": "cancelled",
            "definition": "The episode of care was cancelled, or withdrawn from service, often selected during the planned stage as the patient may have gone elsewhere, or the circumstances have changed and the organization is unable to provide the care. It indicates that services terminated outside the planned/expected workflow.",
            "display": "Cancelled",
        }
    )
    """
    Cancelled

    The episode of care was cancelled, or withdrawn from service, often selected during the planned stage as the patient may have gone elsewhere, or the circumstances have changed and the organization is unable to provide the care. It indicates that services terminated outside the planned/expected workflow.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "This instance should not have been part of this patient's medical record.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    This instance should not have been part of this patient's medical record.
    """

    class Meta:
        resource = _resource
