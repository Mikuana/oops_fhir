from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchSubjectStatus"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchSubjectStatus:
    """
    ResearchSubjectStatus

    Indicates the progression of a study subject through a study.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/research-subject-status
    """

    candidate = CodeSystemConcept(
        {
            "code": "candidate",
            "definition": "An identified person that can be considered for inclusion in a study.",
            "display": "Candidate",
        }
    )
    """
    Candidate

    An identified person that can be considered for inclusion in a study.
    """

    eligible = CodeSystemConcept(
        {
            "code": "eligible",
            "definition": "A person that has met the eligibility criteria for inclusion in a study.",
            "display": "Eligible",
        }
    )
    """
    Eligible

    A person that has met the eligibility criteria for inclusion in a study.
    """

    follow_up = CodeSystemConcept(
        {
            "code": "follow-up",
            "definition": "A person is no longer receiving study intervention and/or being evaluated with tests and procedures according to the protocol, but they are being monitored on a protocol-prescribed schedule.",
            "display": "Follow-up",
        }
    )
    """
    Follow-up

    A person is no longer receiving study intervention and/or being evaluated with tests and procedures according to the protocol, but they are being monitored on a protocol-prescribed schedule.
    """

    ineligible = CodeSystemConcept(
        {
            "code": "ineligible",
            "definition": "A person who did not meet one or more criteria required for participation in a study is considered to have failed screening or\nis ineligible for the study.",
            "display": "Ineligible",
        }
    )
    """
    Ineligible

    A person who did not meet one or more criteria required for participation in a study is considered to have failed screening or
is ineligible for the study.
    """

    not_registered = CodeSystemConcept(
        {
            "code": "not-registered",
            "definition": "A person for whom registration was not completed.",
            "display": "Not Registered",
        }
    )
    """
    Not Registered

    A person for whom registration was not completed.
    """

    off_study = CodeSystemConcept(
        {
            "code": "off-study",
            "definition": "A person that has ended their participation on a study either because their treatment/observation is complete or through not\nresponding, withdrawal, non-compliance and/or adverse event.",
            "display": "Off-study",
        }
    )
    """
    Off-study

    A person that has ended their participation on a study either because their treatment/observation is complete or through not
responding, withdrawal, non-compliance and/or adverse event.
    """

    on_study = CodeSystemConcept(
        {
            "code": "on-study",
            "definition": "A person that is enrolled or registered on a study.",
            "display": "On-study",
        }
    )
    """
    On-study

    A person that is enrolled or registered on a study.
    """

    on_study_intervention = CodeSystemConcept(
        {
            "code": "on-study-intervention",
            "definition": "The person is receiving the treatment or participating in an activity (e.g. yoga, diet, etc.) that the study is evaluating.",
            "display": "On-study-intervention",
        }
    )
    """
    On-study-intervention

    The person is receiving the treatment or participating in an activity (e.g. yoga, diet, etc.) that the study is evaluating.
    """

    on_study_observation = CodeSystemConcept(
        {
            "code": "on-study-observation",
            "definition": 'The subject is being evaluated via tests and assessments according to the study calendar, but is not receiving any intervention. Note that this state is study-dependent and might not exist in all studies.  A synonym for this is "short-term follow-up".',
            "display": "On-study-observation",
        }
    )
    """
    On-study-observation

    The subject is being evaluated via tests and assessments according to the study calendar, but is not receiving any intervention. Note that this state is study-dependent and might not exist in all studies.  A synonym for this is "short-term follow-up".
    """

    pending_on_study = CodeSystemConcept(
        {
            "code": "pending-on-study",
            "definition": "A person is pre-registered for a study.",
            "display": "Pending on-study",
        }
    )
    """
    Pending on-study

    A person is pre-registered for a study.
    """

    potential_candidate = CodeSystemConcept(
        {
            "code": "potential-candidate",
            "definition": "A person that is potentially eligible for participation in the study.",
            "display": "Potential Candidate",
        }
    )
    """
    Potential Candidate

    A person that is potentially eligible for participation in the study.
    """

    screening = CodeSystemConcept(
        {
            "code": "screening",
            "definition": "A person who is being evaluated for eligibility for a study.",
            "display": "Screening",
        }
    )
    """
    Screening

    A person who is being evaluated for eligibility for a study.
    """

    withdrawn = CodeSystemConcept(
        {
            "code": "withdrawn",
            "definition": "The person has withdrawn their participation in the study before registration.",
            "display": "Withdrawn",
        }
    )
    """
    Withdrawn

    The person has withdrawn their participation in the study before registration.
    """

    class Meta:
        resource = _resource
