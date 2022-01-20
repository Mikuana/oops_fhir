from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResearchStudyPhase"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResearchStudyPhase:
    """
    ResearchStudyPhase

    Codes for the stage in the progression of a therapy from initial
experimental use in humans in clinical trials to post-market evaluation.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/research-study-phase
    """

    n_a = CodeSystemConcept(
        {
            "code": "n-a",
            "definition": "Trials without phases (for example, studies of devices or behavioral interventions).",
            "display": "N/A",
        }
    )
    """
    N/A

    Trials without phases (for example, studies of devices or behavioral interventions).
    """

    early_phase_1 = CodeSystemConcept(
        {
            "code": "early-phase-1",
            "definition": "Designation for optional exploratory trials conducted in accordance with the United States Food and Drug Administration's (FDA) 2006 Guidance on Exploratory Investigational New Drug (IND) Studies. Formerly called Phase 0.",
            "display": "Early Phase 1",
        }
    )
    """
    Early Phase 1

    Designation for optional exploratory trials conducted in accordance with the United States Food and Drug Administration's (FDA) 2006 Guidance on Exploratory Investigational New Drug (IND) Studies. Formerly called Phase 0.
    """

    phase_1 = CodeSystemConcept(
        {
            "code": "phase-1",
            "definition": "Includes initial studies to determine the metabolism and pharmacologic actions of drugs in humans, the side effects associated with increasing doses, and to gain early evidence of effectiveness; may include healthy participants and/or patients.",
            "display": "Phase 1",
        }
    )
    """
    Phase 1

    Includes initial studies to determine the metabolism and pharmacologic actions of drugs in humans, the side effects associated with increasing doses, and to gain early evidence of effectiveness; may include healthy participants and/or patients.
    """

    phase_1_phase_2 = CodeSystemConcept(
        {
            "code": "phase-1-phase-2",
            "definition": "Trials that are a combination of phases 1 and 2.",
            "display": "Phase 1/Phase 2",
        }
    )
    """
    Phase 1/Phase 2

    Trials that are a combination of phases 1 and 2.
    """

    phase_2 = CodeSystemConcept(
        {
            "code": "phase-2",
            "definition": "Includes controlled clinical studies conducted to evaluate the effectiveness of the drug for a particular indication or indications in participants with the disease or condition under study and to determine the common short-term side effects and risks.",
            "display": "Phase 2",
        }
    )
    """
    Phase 2

    Includes controlled clinical studies conducted to evaluate the effectiveness of the drug for a particular indication or indications in participants with the disease or condition under study and to determine the common short-term side effects and risks.
    """

    phase_2_phase_3 = CodeSystemConcept(
        {
            "code": "phase-2-phase-3",
            "definition": "Trials that are a combination of phases 2 and 3.",
            "display": "Phase 2/Phase 3",
        }
    )
    """
    Phase 2/Phase 3

    Trials that are a combination of phases 2 and 3.
    """

    phase_3 = CodeSystemConcept(
        {
            "code": "phase-3",
            "definition": "Includes trials conducted after preliminary evidence suggesting effectiveness of the drug has been obtained, and are intended to gather additional information to evaluate the overall benefit-risk relationship of the drug.",
            "display": "Phase 3",
        }
    )
    """
    Phase 3

    Includes trials conducted after preliminary evidence suggesting effectiveness of the drug has been obtained, and are intended to gather additional information to evaluate the overall benefit-risk relationship of the drug.
    """

    phase_4 = CodeSystemConcept(
        {
            "code": "phase-4",
            "definition": "Studies of FDA-approved drugs to delineate additional information including the drug's risks, benefits, and optimal use.",
            "display": "Phase 4",
        }
    )
    """
    Phase 4

    Studies of FDA-approved drugs to delineate additional information including the drug's risks, benefits, and optimal use.
    """

    class Meta:
        resource = _resource
