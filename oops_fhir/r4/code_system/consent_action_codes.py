from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ConsentActionCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ConsentActionCodes:
    """
    Consent Action Codes

    This value set includes sample Consent Action codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://terminology.hl7.org/CodeSystem/consentaction
    """

    collect = CodeSystemConcept(
        {
            "code": "collect",
            "definition": "Gather retrieved information for storage",
            "display": "Collect",
        }
    )
    """
    Collect

    Gather retrieved information for storage
    """

    access = CodeSystemConcept(
        {
            "code": "access",
            "definition": "Retrieval without permitting collection, use or disclosure. e.g., no screen-scraping for collection, use or disclosure (view-only access)",
            "display": "Access",
        }
    )
    """
    Access

    Retrieval without permitting collection, use or disclosure. e.g., no screen-scraping for collection, use or disclosure (view-only access)
    """

    use = CodeSystemConcept(
        {
            "code": "use",
            "definition": "Utilize the retrieved information",
            "display": "Use",
        }
    )
    """
    Use

    Utilize the retrieved information
    """

    disclose = CodeSystemConcept(
        {
            "code": "disclose",
            "definition": "Transfer retrieved information",
            "display": "Disclose",
        }
    )
    """
    Disclose

    Transfer retrieved information
    """

    correct = CodeSystemConcept(
        {
            "code": "correct",
            "definition": "Allow retrieval of a patient's information for the purpose of update or rectify",
            "display": "Access and Correct",
        }
    )
    """
    Access and Correct

    Allow retrieval of a patient's information for the purpose of update or rectify
    """

    class Meta:
        resource = _resource
