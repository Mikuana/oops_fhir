from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FHIRRestfulInteractions"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FHIRRestfulInteractions:
    """
    None

    The set of interactions defined by the RESTful part of the FHIR
specification.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/restful-interaction
    """

    read = CodeSystemConcept(
        {
            "code": "read",
            "definition": "Read the current state of the resource.",
            "display": "read",
        }
    )
    """
    read

    Read the current state of the resource.
    """

    vread = CodeSystemConcept(
        {
            "code": "vread",
            "definition": "Read the state of a specific version of the resource.",
            "display": "vread",
        }
    )
    """
    vread

    Read the state of a specific version of the resource.
    """

    update = CodeSystemConcept(
        {
            "code": "update",
            "definition": "Update an existing resource by its id (or create it if it is new).",
            "display": "update",
        }
    )
    """
    update

    Update an existing resource by its id (or create it if it is new).
    """

    patch = CodeSystemConcept(
        {
            "code": "patch",
            "definition": "Update an existing resource by posting a set of changes to it.",
            "display": "patch",
        }
    )
    """
    patch

    Update an existing resource by posting a set of changes to it.
    """

    delete = CodeSystemConcept(
        {"code": "delete", "definition": "Delete a resource.", "display": "delete"}
    )
    """
    delete

    Delete a resource.
    """

    history = CodeSystemConcept(
        {
            "code": "history",
            "concept": [
                {
                    "code": "history-instance",
                    "definition": "Retrieve the change history for a particular resource.",
                    "display": "history-instance",
                },
                {
                    "code": "history-type",
                    "definition": "Retrieve the change history for all resources of a particular type.",
                    "display": "history-type",
                },
                {
                    "code": "history-system",
                    "definition": "Retrieve the change history for all resources on a system.",
                    "display": "history-system",
                },
            ],
            "definition": "Retrieve the change history for a particular resource, type of resource, or the entire system.",
            "display": "history",
        }
    )
    """
    history

    Retrieve the change history for a particular resource, type of resource, or the entire system.
    """

    create = CodeSystemConcept(
        {
            "code": "create",
            "definition": "Create a new resource with a server assigned id.",
            "display": "create",
        }
    )
    """
    create

    Create a new resource with a server assigned id.
    """

    search = CodeSystemConcept(
        {
            "code": "search",
            "concept": [
                {
                    "code": "search-type",
                    "definition": "Search all resources of the specified type based on some filter criteria.",
                    "display": "search-type",
                },
                {
                    "code": "search-system",
                    "definition": "Search all resources based on some filter criteria.",
                    "display": "search-system",
                },
            ],
            "definition": "Search a resource type or all resources based on some filter criteria.",
            "display": "search",
        }
    )
    """
    search

    Search a resource type or all resources based on some filter criteria.
    """

    capabilities = CodeSystemConcept(
        {
            "code": "capabilities",
            "definition": "Get a Capability Statement for the system.",
            "display": "capabilities",
        }
    )
    """
    capabilities

    Get a Capability Statement for the system.
    """

    transaction = CodeSystemConcept(
        {
            "code": "transaction",
            "definition": "Update, create or delete a set of resources as a single transaction.",
            "display": "transaction",
        }
    )
    """
    transaction

    Update, create or delete a set of resources as a single transaction.
    """

    batch = CodeSystemConcept(
        {
            "code": "batch",
            "definition": "perform a set of a separate interactions in a single http operation",
            "display": "batch",
        }
    )
    """
    batch

    perform a set of a separate interactions in a single http operation
    """

    operation = CodeSystemConcept(
        {
            "code": "operation",
            "definition": "Perform an operation as defined by an OperationDefinition.",
            "display": "operation",
        }
    )
    """
    operation

    Perform an operation as defined by an OperationDefinition.
    """

    class Meta:
        resource = _resource
