from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceCertainty"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceCertainty:
    """
    AllergyIntoleranceCertainty

    Statement about the degree of clinical certainty that a specific
substance was the cause of the manifestation in a reaction event.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/reaction-event-certainty
    """

    unlikely = CodeSystemConcept(
        {
            "code": "unlikely",
            "definition": "There is a low level of clinical certainty that the reaction was caused by the identified substance.",
            "display": "Unlikely",
        }
    )
    """
    Unlikely

    There is a low level of clinical certainty that the reaction was caused by the identified substance.
    """

    likely = CodeSystemConcept(
        {
            "code": "likely",
            "definition": "There is a high level of clinical certainty that the reaction was caused by the identified substance.",
            "display": "Likely",
        }
    )
    """
    Likely

    There is a high level of clinical certainty that the reaction was caused by the identified substance.
    """

    confirmed = CodeSystemConcept(
        {
            "code": "confirmed",
            "definition": "There is a very high level of clinical certainty that the reaction was due to the identified substance, which may include clinical evidence by testing or rechallenge.",
            "display": "Confirmed",
        }
    )
    """
    Confirmed

    There is a very high level of clinical certainty that the reaction was due to the identified substance, which may include clinical evidence by testing or rechallenge.
    """

    unknown = CodeSystemConcept(
        {
            "code": "unknown",
            "definition": "The clinical certainty that the reaction was caused by the identified substance is unknown.  It is an explicit assertion that certainty is not known.",
            "display": "Unknown",
        }
    )
    """
    Unknown

    The clinical certainty that the reaction was caused by the identified substance is unknown.  It is an explicit assertion that certainty is not known.
    """

    class Meta:
        resource = _resource
