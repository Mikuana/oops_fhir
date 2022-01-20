from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["LinkType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class LinkType:
    """
    LinkType

    The type of link between this patient resource and another patient
resource.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/link-type
    """

    replaced_by = CodeSystemConcept(
        {
            "code": "replaced-by",
            "definition": "The patient resource containing this link must no longer be used. The link points forward to another patient resource that must be used in lieu of the patient resource that contains this link.",
            "designation": [{"language": "nl", "value": "Vervangen door"}],
            "display": "Replaced-by",
        }
    )
    """
    Replaced-by

    The patient resource containing this link must no longer be used. The link points forward to another patient resource that must be used in lieu of the patient resource that contains this link.
    """

    replaces = CodeSystemConcept(
        {
            "code": "replaces",
            "definition": "The patient resource containing this link is the current active patient record. The link points back to an inactive patient resource that has been merged into this resource, and should be consulted to retrieve additional referenced information.",
            "designation": [{"language": "nl", "value": "Vervangt"}],
            "display": "Replaces",
        }
    )
    """
    Replaces

    The patient resource containing this link is the current active patient record. The link points back to an inactive patient resource that has been merged into this resource, and should be consulted to retrieve additional referenced information.
    """

    refer = CodeSystemConcept(
        {
            "code": "refer",
            "definition": "The patient resource containing this link is in use and valid but not considered the main source of information about a patient. The link points forward to another patient resource that should be consulted to retrieve additional patient information.",
            "designation": [{"language": "nl", "value": "Verwijzing"}],
            "display": "Refer",
        }
    )
    """
    Refer

    The patient resource containing this link is in use and valid but not considered the main source of information about a patient. The link points forward to another patient resource that should be consulted to retrieve additional patient information.
    """

    seealso = CodeSystemConcept(
        {
            "code": "seealso",
            "definition": "The patient resource containing this link is in use and valid, but points to another patient resource that is known to contain data about the same person. Data in this resource might overlap or contradict information found in the other patient resource. This link does not indicate any relative importance of the resources concerned, and both should be regarded as equally valid.",
            "designation": [{"language": "nl", "value": "Zie ook"}],
            "display": "See also",
        }
    )
    """
    See also

    The patient resource containing this link is in use and valid, but points to another patient resource that is known to contain data about the same person. Data in this resource might overlap or contradict information found in the other patient resource. This link does not indicate any relative importance of the resources concerned, and both should be regarded as equally valid.
    """

    class Meta:
        resource = _resource
