from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AdditionalMaterialCodes"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AdditionalMaterialCodes:
    """
    Additional Material Codes

    This value set includes sample additional material type codes.

    Status: draft - Version: 4.0.1

    Copyright This is an example set.

    http://hl7.org/fhir/additionalmaterials
    """

    xray = CodeSystemConcept({"code": "xray", "definition": "XRay", "display": "XRay"})
    """
    XRay

    XRay
    """

    image = CodeSystemConcept(
        {"code": "image", "definition": "Image", "display": "Image"}
    )
    """
    Image

    Image
    """

    email = CodeSystemConcept(
        {"code": "email", "definition": "Email", "display": "Email"}
    )
    """
    Email

    Email
    """

    model = CodeSystemConcept(
        {"code": "model", "definition": "Model", "display": "Model"}
    )
    """
    Model

    Model
    """

    document = CodeSystemConcept(
        {"code": "document", "definition": "Document", "display": "Document"}
    )
    """
    Document

    Document
    """

    other = CodeSystemConcept(
        {"code": "other", "definition": "Other", "display": "Other"}
    )
    """
    Other

    Other
    """

    class Meta:
        resource = _resource
