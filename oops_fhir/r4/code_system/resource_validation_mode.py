from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["ResourceValidationMode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class ResourceValidationMode:
    """
    ResourceValidationMode

    Codes indicating the type of validation to perform.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/resource-validation-mode
    """

    create = CodeSystemConcept(
        {
            "code": "create",
            "definition": "The server checks the content, and then checks that the content would be acceptable as a create (e.g. that the content would not violate any uniqueness constraints).",
            "display": "Validate for Create",
        }
    )
    """
    Validate for Create

    The server checks the content, and then checks that the content would be acceptable as a create (e.g. that the content would not violate any uniqueness constraints).
    """

    update = CodeSystemConcept(
        {
            "code": "update",
            "definition": "The server checks the content, and then checks that it would accept it as an update against the nominated specific resource (e.g. that there are no changes to immutable fields the server does not allow to change and checking version integrity if appropriate).",
            "display": "Validate for Update",
        }
    )
    """
    Validate for Update

    The server checks the content, and then checks that it would accept it as an update against the nominated specific resource (e.g. that there are no changes to immutable fields the server does not allow to change and checking version integrity if appropriate).
    """

    delete = CodeSystemConcept(
        {
            "code": "delete",
            "definition": "The server ignores the content and checks that the nominated resource is allowed to be deleted (e.g. checking referential integrity rules).",
            "display": "Validate for Delete",
        }
    )
    """
    Validate for Delete

    The server ignores the content and checks that the nominated resource is allowed to be deleted (e.g. checking referential integrity rules).
    """

    profile = CodeSystemConcept(
        {
            "code": "profile",
            "definition": "The server checks an existing resource (must be nominated by id, not provided as a parameter) as valid against the nominated profile.",
            "display": "Validate Against a Profile",
        }
    )
    """
    Validate Against a Profile

    The server checks an existing resource (must be nominated by id, not provided as a parameter) as valid against the nominated profile.
    """

    class Meta:
        resource = _resource
