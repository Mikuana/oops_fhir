from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ClaimInformationCategoryCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ClaimInformationCategoryCodes:
    """
    Claim Information Category Codes

    This value set includes sample Information Category codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/claiminformationcategory
    """

    info = CodeSystemConcept(
        {
            "code": "info",
            "definition": "Codes conveying additional situation and condition information.",
            "display": "Information",
        }
    )
    """
    Information

    Codes conveying additional situation and condition information.
    """

    discharge = CodeSystemConcept(
        {
            "code": "discharge",
            "definition": "Discharge status and discharge to locations.",
            "display": "Discharge",
        }
    )
    """
    Discharge

    Discharge status and discharge to locations.
    """

    onset = CodeSystemConcept(
        {
            "code": "onset",
            "definition": "Period, start or end dates of aspects of the Condition.",
            "display": "Onset",
        }
    )
    """
    Onset

    Period, start or end dates of aspects of the Condition.
    """

    related = CodeSystemConcept(
        {
            "code": "related",
            "definition": "Nature and date of the related event e.g. Last exam, service, X-ray etc.",
            "display": "Related Services",
        }
    )
    """
    Related Services

    Nature and date of the related event e.g. Last exam, service, X-ray etc.
    """

    exception = CodeSystemConcept(
        {
            "code": "exception",
            "definition": "Insurance policy exceptions.",
            "display": "Exception",
        }
    )
    """
    Exception

    Insurance policy exceptions.
    """

    material = CodeSystemConcept(
        {
            "code": "material",
            "definition": "Materials being forwarded, e.g. Models, molds, images, documents.",
            "display": "Materials Forwarded",
        }
    )
    """
    Materials Forwarded

    Materials being forwarded, e.g. Models, molds, images, documents.
    """

    attachment = CodeSystemConcept(
        {
            "code": "attachment",
            "definition": "Materials attached such as images, documents and resources.",
            "display": "Attachment",
        }
    )
    """
    Attachment

    Materials attached such as images, documents and resources.
    """

    missingtooth = CodeSystemConcept(
        {
            "code": "missingtooth",
            "definition": "Teeth which are missing for any reason, for example: prior extraction, never developed.",
            "display": "Missing Tooth",
        }
    )
    """
    Missing Tooth

    Teeth which are missing for any reason, for example: prior extraction, never developed.
    """

    prosthesis = CodeSystemConcept(
        {
            "code": "prosthesis",
            "definition": "The type of prosthesis and date of supply if a previously supplied prosthesis.",
            "display": "Prosthesis",
        }
    )
    """
    Prosthesis

    The type of prosthesis and date of supply if a previously supplied prosthesis.
    """

    other = CodeSystemConcept(
        {
            "code": "other",
            "definition": "Other information identified by the type.system.",
            "display": "Other",
        }
    )
    """
    Other

    Other information identified by the type.system.
    """

    hospitalized = CodeSystemConcept(
        {
            "code": "hospitalized",
            "definition": "An indication that the patient was hospitalized, the period if known otherwise a Yes/No (boolean).",
            "display": "Hospitalized",
        }
    )
    """
    Hospitalized

    An indication that the patient was hospitalized, the period if known otherwise a Yes/No (boolean).
    """

    employmentimpacted = CodeSystemConcept(
        {
            "code": "employmentimpacted",
            "definition": "An indication that the patient was unable to work, the period if known otherwise a Yes/No (boolean).",
            "display": "EmploymentImpacted",
        }
    )
    """
    EmploymentImpacted

    An indication that the patient was unable to work, the period if known otherwise a Yes/No (boolean).
    """

    externalcause = CodeSystemConcept(
        {
            "code": "externalcause",
            "definition": "The external cause of an illness or injury.",
            "display": "External Caause",
        }
    )
    """
    External Caause

    The external cause of an illness or injury.
    """

    patientreasonforvisit = CodeSystemConcept(
        {
            "code": "patientreasonforvisit",
            "definition": "The reason for the patient visit.",
            "display": "Patient Reason for Visit",
        }
    )
    """
    Patient Reason for Visit

    The reason for the patient visit.
    """

    class Meta:
        resource = _resource
