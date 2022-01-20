from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdmitSource"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdmitSource:
    """
    Admit source

    This value set defines a set of codes that can be used to indicate from
where the patient came in.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/admit-source
    """

    hosp_trans = CodeSystemConcept(
        {
            "code": "hosp-trans",
            "definition": "The Patient has been transferred from another hospital for this encounter.",
            "display": "Transferred from other hospital",
        }
    )
    """
    Transferred from other hospital

    The Patient has been transferred from another hospital for this encounter.
    """

    emd = CodeSystemConcept(
        {
            "code": "emd",
            "definition": "The patient has been transferred from the emergency department within the hospital. This is typically used in the transition to an inpatient encounter",
            "display": "From accident/emergency department",
        }
    )
    """
    From accident/emergency department

    The patient has been transferred from the emergency department within the hospital. This is typically used in the transition to an inpatient encounter
    """

    outp = CodeSystemConcept(
        {
            "code": "outp",
            "definition": "The patient has been transferred from an outpatient department within the hospital.",
            "display": "From outpatient department",
        }
    )
    """
    From outpatient department

    The patient has been transferred from an outpatient department within the hospital.
    """

    born = CodeSystemConcept(
        {
            "code": "born",
            "definition": "The patient is a newborn and the encounter will track the baby related activities (as opposed to the Mothers encounter - that may be associated using the newborn encounters partof property)",
            "display": "Born in hospital",
        }
    )
    """
    Born in hospital

    The patient is a newborn and the encounter will track the baby related activities (as opposed to the Mothers encounter - that may be associated using the newborn encounters partof property)
    """

    gp = CodeSystemConcept(
        {
            "code": "gp",
            "definition": "The patient has been admitted due to a referred from a General Practitioner.",
            "display": "General Practitioner referral",
        }
    )
    """
    General Practitioner referral

    The patient has been admitted due to a referred from a General Practitioner.
    """

    mp = CodeSystemConcept(
        {
            "code": "mp",
            "definition": "The patient has been admitted due to a referred from a Specialist (as opposed to a General Practitioner).",
            "display": "Medical Practitioner/physician referral",
        }
    )
    """
    Medical Practitioner/physician referral

    The patient has been admitted due to a referred from a Specialist (as opposed to a General Practitioner).
    """

    nursing = CodeSystemConcept(
        {
            "code": "nursing",
            "definition": "The patient has been transferred from a nursing home.",
            "display": "From nursing home",
        }
    )
    """
    From nursing home

    The patient has been transferred from a nursing home.
    """

    psych = CodeSystemConcept(
        {
            "code": "psych",
            "definition": "The patient has been transferred from a psychiatric facility.",
            "display": "From psychiatric hospital",
        }
    )
    """
    From psychiatric hospital

    The patient has been transferred from a psychiatric facility.
    """

    rehab = CodeSystemConcept(
        {
            "code": "rehab",
            "definition": "The patient has been transferred from a rehabilitation facility or clinic.",
            "display": "From rehabilitation facility",
        }
    )
    """
    From rehabilitation facility

    The patient has been transferred from a rehabilitation facility or clinic.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "The patient has been admitted from a source otherwise not specified here.",
            "display": "Other",
        }
    )
    """
    Other

    The patient has been admitted from a source otherwise not specified here.
    """

    class Meta:
        resource = _resource
