from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["SNOMEDCTReasonMedicationNotGivenCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class SNOMEDCTReasonMedicationNotGivenCodes:
    """
    SNOMED CT Reason Medication Not Given Codes

    This value set includes all medication refused, medication not
administered, and non-administration of necessary drug or medicine codes
from SNOMED CT - provided as an exemplar value set.

    Status: draft - Version: 4.0.1

    Copyright This value set includes content from SNOMED CT, which is copyright 2002 International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement.

    http://hl7.org/fhir/reason-medication-not-given
    """

    a = CodeSystemConcept(
        {"code": "a", "definition": "No reason known.", "display": "None"}
    )
    """
    None

    No reason known.
    """

    b = CodeSystemConcept(
        {
            "code": "b",
            "definition": "The patient was not available when the dose was scheduled.",
            "display": "Away",
        }
    )
    """
    Away

    The patient was not available when the dose was scheduled.
    """

    c = CodeSystemConcept(
        {
            "code": "c",
            "definition": "The patient was asleep when the dose was scheduled.",
            "display": "Asleep",
        }
    )
    """
    Asleep

    The patient was asleep when the dose was scheduled.
    """

    d = CodeSystemConcept(
        {
            "code": "d",
            "definition": "The patient was given the medication and immediately vomited it back.",
            "display": "Vomit",
        }
    )
    """
    Vomit

    The patient was given the medication and immediately vomited it back.
    """

    class Meta:
        resource = _resource
