from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3ActInvoiceElementModifier"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3ActInvoiceElementModifier:
    """
    v3 Code System ActInvoiceElementModifier

     Processing consideration and clarification codes.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-ActInvoiceElementModifier
    """

    eform = CodeSystemConcept(
        {
            "code": "EFORM",
            "definition": "Electronic form with supporting information to follow.",
            "display": "Electronic Form To Follow",
        }
    )
    """
    Electronic Form To Follow

    Electronic form with supporting information to follow.
    """

    fax = CodeSystemConcept(
        {
            "code": "FAX",
            "definition": "Fax with supporting information to follow.",
            "display": "Fax To Follow",
        }
    )
    """
    Fax To Follow

    Fax with supporting information to follow.
    """

    linv = CodeSystemConcept(
        {
            "code": "LINV",
            "definition": "Represents the last invoice from the perspective of the provider.",
            "display": "Last Invoice",
        }
    )
    """
    Last Invoice

    Represents the last invoice from the perspective of the provider.
    """

    paper = CodeSystemConcept(
        {
            "code": "PAPER",
            "definition": "Paper documentation (or other physical format) with supporting information to follow.",
            "display": "Paper Documentation To Follow",
        }
    )
    """
    Paper Documentation To Follow

    Paper documentation (or other physical format) with supporting information to follow.
    """

    class Meta:
        resource = _resource
