from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AllergyIntoleranceVerificationStatusCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AllergyIntoleranceVerificationStatusCodes:
    """
    AllergyIntolerance Verification Status Codes

    Preferred value set for AllergyIntolerance Verification Status.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/allergyintolerance-verification
    """

    unconfirmed = CodeSystemConcept(
        {
            "code": "unconfirmed",
            "definition": "A low level of certainty about the propensity for a reaction to the identified substance.",
            "display": "Unconfirmed",
        }
    )
    """
    Unconfirmed

    A low level of certainty about the propensity for a reaction to the identified substance.
    """

    confirmed = CodeSystemConcept(
        {
            "code": "confirmed",
            "definition": "A high level of certainty about the propensity for a reaction to the identified substance, which may include clinical evidence by testing or rechallenge.",
            "display": "Confirmed",
        }
    )
    """
    Confirmed

    A high level of certainty about the propensity for a reaction to the identified substance, which may include clinical evidence by testing or rechallenge.
    """

    refuted = CodeSystemConcept(
        {
            "code": "refuted",
            "definition": "A propensity for a reaction to the identified substance has been disputed or disproven with a sufficient level of clinical certainty to justify invalidating the assertion. This might or might not include testing or rechallenge.",
            "display": "Refuted",
        }
    )
    """
    Refuted

    A propensity for a reaction to the identified substance has been disputed or disproven with a sufficient level of clinical certainty to justify invalidating the assertion. This might or might not include testing or rechallenge.
    """

    entered_in_error = CodeSystemConcept(
        {
            "code": "entered-in-error",
            "definition": "The statement was entered in error and is not valid.",
            "display": "Entered in Error",
        }
    )
    """
    Entered in Error

    The statement was entered in error and is not valid.
    """

    class Meta:
        resource = _resource
