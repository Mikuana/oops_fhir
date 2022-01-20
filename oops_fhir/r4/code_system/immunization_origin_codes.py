from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ImmunizationOriginCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ImmunizationOriginCodes:
    """
    Immunization Origin Codes

    The value set to instantiate this attribute should be drawn from a
terminologically robust code system that consists of or contains
concepts to support describing the source of the data when the report of
the immunization event is not based on information from the person,
entity or organization who administered the vaccine. This value set is
provided as a suggestive example.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/immunization-origin
    """

    provider = CodeSystemConcept(
        {
            "code": "provider",
            "definition": "The data for the immunization event originated with another provider.",
            "display": "Other Provider",
        }
    )
    """
    Other Provider

    The data for the immunization event originated with another provider.
    """

    record = CodeSystemConcept(
        {
            "code": "record",
            "definition": "The data for the immunization event originated with a written record for the patient.",
            "display": "Written Record",
        }
    )
    """
    Written Record

    The data for the immunization event originated with a written record for the patient.
    """

    recall = CodeSystemConcept(
        {
            "code": "recall",
            "definition": "The data for the immunization event originated from the recollection of the patient or parent/guardian of the patient.",
            "display": "Parent/Guardian/Patient Recall",
        }
    )
    """
    Parent/Guardian/Patient Recall

    The data for the immunization event originated from the recollection of the patient or parent/guardian of the patient.
    """

    school = CodeSystemConcept(
        {
            "code": "school",
            "definition": "The data for the immunization event originated with a school record for the patient.",
            "display": "School Record",
        }
    )
    """
    School Record

    The data for the immunization event originated with a school record for the patient.
    """

    jurisdiction = CodeSystemConcept(
        {
            "code": "jurisdiction",
            "definition": "The data for the immunization event originated with an immunization information system (IIS) or registry operating within the jurisdiction.",
            "display": "Jurisdictional IIS",
        }
    )
    """
    Jurisdictional IIS

    The data for the immunization event originated with an immunization information system (IIS) or registry operating within the jurisdiction.
    """

    class Meta:
        resource = _resource
