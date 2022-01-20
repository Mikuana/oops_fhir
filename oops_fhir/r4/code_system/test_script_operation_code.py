from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["TestScriptOperationCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class TestScriptOperationCode:
    """
    Test script operation code

    This value set defines a set of codes that are used to indicate the
supported operations of a testing engine or tool.

    Status: draft - Version: 4.0.1

    Copyright None

    http://terminology.hl7.org/CodeSystem/testscript-operation-codes
    """

    read = CodeSystemConcept(
        {
            "code": "read",
            "definition": "Read the current state of the resource.",
            "display": "Read",
        }
    )
    """
    Read

    Read the current state of the resource.
    """

    vread = CodeSystemConcept(
        {
            "code": "vread",
            "definition": "Read the state of a specific version of the resource.",
            "display": "Version Read",
        }
    )
    """
    Version Read

    Read the state of a specific version of the resource.
    """

    update = CodeSystemConcept(
        {
            "code": "update",
            "definition": "Update an existing resource by its id.",
            "display": "Update",
        }
    )
    """
    Update

    Update an existing resource by its id.
    """

    update_create = CodeSystemConcept(
        {
            "code": "updateCreate",
            "definition": "Update an existing resource by its id (or create it if it is new).",
            "display": "Create using Update",
        }
    )
    """
    Create using Update

    Update an existing resource by its id (or create it if it is new).
    """

    patch = CodeSystemConcept(
        {
            "code": "patch",
            "definition": "Patch an existing resource by its id.",
            "display": "Patch",
        }
    )
    """
    Patch

    Patch an existing resource by its id.
    """

    delete = CodeSystemConcept(
        {"code": "delete", "definition": "Delete a resource.", "display": "Delete"}
    )
    """
    Delete

    Delete a resource.
    """

    delete_cond_single = CodeSystemConcept(
        {
            "code": "deleteCondSingle",
            "definition": "Conditionally delete a single resource based on search parameters.",
            "display": "Conditional Delete Single",
        }
    )
    """
    Conditional Delete Single

    Conditionally delete a single resource based on search parameters.
    """

    delete_cond_multiple = CodeSystemConcept(
        {
            "code": "deleteCondMultiple",
            "definition": "Conditionally delete one or more resources based on search parameters.",
            "display": "Conditional Delete Multiple",
        }
    )
    """
    Conditional Delete Multiple

    Conditionally delete one or more resources based on search parameters.
    """

    history = CodeSystemConcept(
        {
            "code": "history",
            "definition": "Retrieve the change history for a particular resource or resource type.",
            "display": "History",
        }
    )
    """
    History

    Retrieve the change history for a particular resource or resource type.
    """

    create = CodeSystemConcept(
        {
            "code": "create",
            "definition": "Create a new resource with a server assigned id.",
            "display": "Create",
        }
    )
    """
    Create

    Create a new resource with a server assigned id.
    """

    search = CodeSystemConcept(
        {
            "code": "search",
            "definition": "Search based on some filter criteria.",
            "display": "Search",
        }
    )
    """
    Search

    Search based on some filter criteria.
    """

    batch = CodeSystemConcept(
        {
            "code": "batch",
            "definition": "Update, create or delete a set of resources as independent actions.",
            "display": "Batch",
        }
    )
    """
    Batch

    Update, create or delete a set of resources as independent actions.
    """

    transaction = CodeSystemConcept(
        {
            "code": "transaction",
            "definition": "Update, create or delete a set of resources as a single transaction.",
            "display": "Transaction",
        }
    )
    """
    Transaction

    Update, create or delete a set of resources as a single transaction.
    """

    capabilities = CodeSystemConcept(
        {
            "code": "capabilities",
            "definition": "Get a capability statement for the system.",
            "display": "Capabilities",
        }
    )
    """
    Capabilities

    Get a capability statement for the system.
    """

    apply = CodeSystemConcept(
        {
            "code": "apply",
            "definition": "Realizes an ActivityDefinition in a specific context",
            "display": "$apply",
        }
    )
    """
    $apply

    Realizes an ActivityDefinition in a specific context
    """

    closure = CodeSystemConcept(
        {
            "code": "closure",
            "definition": "Closure Table Maintenance",
            "display": "$closure",
        }
    )
    """
    $closure

    Closure Table Maintenance
    """

    find_matches = CodeSystemConcept(
        {
            "code": "find-matches",
            "definition": "Finding Codes based on supplied properties",
            "display": "$find-matches",
        }
    )
    """
    $find-matches

    Finding Codes based on supplied properties
    """

    conforms = CodeSystemConcept(
        {
            "code": "conforms",
            "definition": "Compare two systems CapabilityStatements",
            "display": "$conforms",
        }
    )
    """
    $conforms

    Compare two systems CapabilityStatements
    """

    data_requirements = CodeSystemConcept(
        {
            "code": "data-requirements",
            "definition": "Aggregates and returns the parameters and data requirements for a resource and all its dependencies as a single module definition",
            "display": "$data-requirements",
        }
    )
    """
    $data-requirements

    Aggregates and returns the parameters and data requirements for a resource and all its dependencies as a single module definition
    """

    document = CodeSystemConcept(
        {
            "code": "document",
            "definition": "Generate a Document",
            "display": "$document",
        }
    )
    """
    $document

    Generate a Document
    """

    evaluate = CodeSystemConcept(
        {
            "code": "evaluate",
            "definition": "Request clinical decision support guidance based on a specific decision support module",
            "display": "$evaluate",
        }
    )
    """
    $evaluate

    Request clinical decision support guidance based on a specific decision support module
    """

    evaluate_measure = CodeSystemConcept(
        {
            "code": "evaluate-measure",
            "definition": "Invoke an eMeasure and obtain the results",
            "display": "$evaluate-measure",
        }
    )
    """
    $evaluate-measure

    Invoke an eMeasure and obtain the results
    """

    everything = CodeSystemConcept(
        {
            "code": "everything",
            "definition": "Return all the related information as described in the Encounter or Patient",
            "display": "$everything",
        }
    )
    """
    $everything

    Return all the related information as described in the Encounter or Patient
    """

    expand = CodeSystemConcept(
        {"code": "expand", "definition": "Value Set Expansion", "display": "$expand"}
    )
    """
    $expand

    Value Set Expansion
    """

    find = CodeSystemConcept(
        {"code": "find", "definition": "Find a functional list", "display": "$find"}
    )
    """
    $find

    Find a functional list
    """

    graphql = CodeSystemConcept(
        {
            "code": "graphql",
            "definition": "Invoke a GraphQL query",
            "display": "$graphql",
        }
    )
    """
    $graphql

    Invoke a GraphQL query
    """

    implements = CodeSystemConcept(
        {
            "code": "implements",
            "definition": "Test if a server implements a client's required operations",
            "display": "$implements",
        }
    )
    """
    $implements

    Test if a server implements a client's required operations
    """

    lastn = CodeSystemConcept(
        {
            "code": "lastn",
            "definition": "Last N Observations Query",
            "display": "$lastn",
        }
    )
    """
    $lastn

    Last N Observations Query
    """

    lookup = CodeSystemConcept(
        {
            "code": "lookup",
            "definition": "Concept Look Up and Decomposition",
            "display": "$lookup",
        }
    )
    """
    $lookup

    Concept Look Up and Decomposition
    """

    match = CodeSystemConcept(
        {
            "code": "match",
            "definition": "Find patient matches using MPI based logic",
            "display": "$match",
        }
    )
    """
    $match

    Find patient matches using MPI based logic
    """

    meta = CodeSystemConcept(
        {
            "code": "meta",
            "definition": "Access a list of profiles, tags, and security labels",
            "display": "$meta",
        }
    )
    """
    $meta

    Access a list of profiles, tags, and security labels
    """

    meta_add = CodeSystemConcept(
        {
            "code": "meta-add",
            "definition": "Add profiles, tags, and security labels to a resource",
            "display": "$meta-add",
        }
    )
    """
    $meta-add

    Add profiles, tags, and security labels to a resource
    """

    meta_delete = CodeSystemConcept(
        {
            "code": "meta-delete",
            "definition": "Delete profiles, tags, and security labels for a resource",
            "display": "$meta-delete",
        }
    )
    """
    $meta-delete

    Delete profiles, tags, and security labels for a resource
    """

    populate = CodeSystemConcept(
        {
            "code": "populate",
            "definition": "Populate Questionnaire",
            "display": "$populate",
        }
    )
    """
    $populate

    Populate Questionnaire
    """

    populatehtml = CodeSystemConcept(
        {
            "code": "populatehtml",
            "definition": "Generate HTML for Questionnaire",
            "display": "$populatehtml",
        }
    )
    """
    $populatehtml

    Generate HTML for Questionnaire
    """

    populatelink = CodeSystemConcept(
        {
            "code": "populatelink",
            "definition": "Generate a link to a Questionnaire completion webpage",
            "display": "$populatelink",
        }
    )
    """
    $populatelink

    Generate a link to a Questionnaire completion webpage
    """

    process_message = CodeSystemConcept(
        {
            "code": "process-message",
            "definition": "Process a message according to the defined event",
            "display": "$process-message",
        }
    )
    """
    $process-message

    Process a message according to the defined event
    """

    questionnaire = CodeSystemConcept(
        {
            "code": "questionnaire",
            "definition": "Build Questionnaire",
            "display": "$questionnaire",
        }
    )
    """
    $questionnaire

    Build Questionnaire
    """

    stats = CodeSystemConcept(
        {"code": "stats", "definition": "Observation Statistics", "display": "$stats"}
    )
    """
    $stats

    Observation Statistics
    """

    subset = CodeSystemConcept(
        {
            "code": "subset",
            "definition": "Fetch a subset of the CapabilityStatement resource",
            "display": "$subset",
        }
    )
    """
    $subset

    Fetch a subset of the CapabilityStatement resource
    """

    subsumes = CodeSystemConcept(
        {
            "code": "subsumes",
            "definition": "CodeSystem Subsumption Testing",
            "display": "$subsumes",
        }
    )
    """
    $subsumes

    CodeSystem Subsumption Testing
    """

    transform = CodeSystemConcept(
        {
            "code": "transform",
            "definition": "Model Instance Transformation",
            "display": "$transform",
        }
    )
    """
    $transform

    Model Instance Transformation
    """

    translate = CodeSystemConcept(
        {
            "code": "translate",
            "definition": "Concept Translation",
            "display": "$translate",
        }
    )
    """
    $translate

    Concept Translation
    """

    validate = CodeSystemConcept(
        {
            "code": "validate",
            "definition": "Validate a resource",
            "display": "$validate",
        }
    )
    """
    $validate

    Validate a resource
    """

    validate_code = CodeSystemConcept(
        {
            "code": "validate-code",
            "definition": "ValueSet based Validation",
            "display": "$validate-code",
        }
    )
    """
    $validate-code

    ValueSet based Validation
    """

    class Meta:
        resource = _resource
