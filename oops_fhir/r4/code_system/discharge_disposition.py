from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DischargeDisposition"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DischargeDisposition:
    """
    Discharge disposition

    This value set defines a set of codes that can be used to where the
patient left the hospital.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/discharge-disposition
    """

    home = CodeSystemConcept(
        {
            "code": "home",
            "definition": "The patient was dicharged and has indicated that they are going to return home afterwards.",
            "display": "Home",
        }
    )
    """
    Home

    The patient was dicharged and has indicated that they are going to return home afterwards.
    """

    alt_home = CodeSystemConcept(
        {
            "code": "alt-home",
            "definition": "The patient was discharged and has indicated that they are going to return home afterwards, but not the patient's home - e.g. a family member's home.",
            "display": "Alternative home",
        }
    )
    """
    Alternative home

    The patient was discharged and has indicated that they are going to return home afterwards, but not the patient's home - e.g. a family member's home.
    """

    other_hcf = CodeSystemConcept(
        {
            "code": "other-hcf",
            "definition": "The patient was transferred to another healthcare facility.",
            "display": "Other healthcare facility",
        }
    )
    """
    Other healthcare facility

    The patient was transferred to another healthcare facility.
    """

    hosp = CodeSystemConcept(
        {
            "code": "hosp",
            "definition": "The patient has been discharged into palliative care.",
            "display": "Hospice",
        }
    )
    """
    Hospice

    The patient has been discharged into palliative care.
    """

    long = CodeSystemConcept(
        {
            "code": "long",
            "definition": "The patient has been discharged into long-term care where is likely to be monitored through an ongoing episode-of-care.",
            "display": "Long-term care",
        }
    )
    """
    Long-term care

    The patient has been discharged into long-term care where is likely to be monitored through an ongoing episode-of-care.
    """

    aadvice = CodeSystemConcept(
        {
            "code": "aadvice",
            "definition": "The patient self discharged against medical advice.",
            "display": "Left against advice",
        }
    )
    """
    Left against advice

    The patient self discharged against medical advice.
    """

    exp = CodeSystemConcept(
        {
            "code": "exp",
            "definition": "The patient has deceased during this encounter.",
            "display": "Expired",
        }
    )
    """
    Expired

    The patient has deceased during this encounter.
    """

    psy = CodeSystemConcept(
        {
            "code": "psy",
            "definition": "The patient has been transferred to a psychiatric facility.",
            "display": "Psychiatric hospital",
        }
    )
    """
    Psychiatric hospital

    The patient has been transferred to a psychiatric facility.
    """

    rehab = CodeSystemConcept(
        {
            "code": "rehab",
            "definition": "The patient was discharged and is to receive post acute care rehabilitation services.",
            "display": "Rehabilitation",
        }
    )
    """
    Rehabilitation

    The patient was discharged and is to receive post acute care rehabilitation services.
    """

    snf = CodeSystemConcept(
        {
            "code": "snf",
            "definition": "The patient has been discharged to a skilled nursing facility for the patient to receive additional care.",
            "display": "Skilled nursing facility",
        }
    )
    """
    Skilled nursing facility

    The patient has been discharged to a skilled nursing facility for the patient to receive additional care.
    """

    oth = CodeSystemConcept(
        {
            "code": "oth",
            "definition": "The discharge disposition has not otherwise defined.",
            "display": "Other",
        }
    )
    """
    Other

    The discharge disposition has not otherwise defined.
    """

    class Meta:
        resource = _resource
