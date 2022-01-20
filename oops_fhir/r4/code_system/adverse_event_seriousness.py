from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdverseEventSeriousness"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdverseEventSeriousness:
    """
    AdverseEventSeriousness

    Overall seriousness of this event for the patient.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/adverse-event-seriousness
    """

    non_serious = CodeSystemConcept(
        {"code": "Non-serious", "definition": "Non-serious.", "display": "Non-serious"}
    )
    """
    Non-serious

    Non-serious.
    """

    serious = CodeSystemConcept(
        {
            "code": "Serious",
            "concept": [
                {
                    "code": "SeriousResultsInDeath",
                    "definition": "Results in death.",
                    "display": "Results in death",
                },
                {
                    "code": "SeriousIsLifeThreatening",
                    "definition": "Is Life-threatening.",
                    "display": "Is Life-threatening",
                },
                {
                    "code": "SeriousResultsInHospitalization",
                    "definition": "Requires inpatient hospitalization or causes prolongation of existing hospitalization.",
                    "display": "Requires or prolongs inpatient hospitalization",
                },
                {
                    "code": "SeriousResultsInDisability",
                    "definition": "Results in persistent or significant disability/incapacity.",
                    "display": "Results in persistent or significant disability/incapacity",
                },
                {
                    "code": "SeriousIsBirthDefect",
                    "definition": "Is a congenital anomaly/birth defect.",
                    "display": "Is a congenital anomaly/birth defect",
                },
                {
                    "code": "SeriousRequiresPreventImpairment",
                    "definition": "Requires intervention to prevent permanent impairment or damage (i.e., an important medical event that requires medical judgement).",
                    "display": "Requires intervention to prevent permanent impairment",
                },
            ],
            "definition": "Serious.",
            "display": "Serious",
        }
    )
    """
    Serious

    Serious.
    """

    class Meta:
        resource = _resource
