from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["StructureMapTransform"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class StructureMapTransform:
    """
    StructureMapTransform

    How data is copied/created.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/map-transform
    """

    create = CodeSystemConcept(
        {
            "code": "create",
            "definition": "create(type : string) - type is passed through to the application on the standard API, and must be known by it.",
            "display": "create",
        }
    )
    """
    create

    create(type : string) - type is passed through to the application on the standard API, and must be known by it.
    """

    copy = CodeSystemConcept(
        {"code": "copy", "definition": "copy(source).", "display": "copy"}
    )
    """
    copy

    copy(source).
    """

    truncate = CodeSystemConcept(
        {
            "code": "truncate",
            "definition": "truncate(source, length) - source must be stringy type.",
            "display": "truncate",
        }
    )
    """
    truncate

    truncate(source, length) - source must be stringy type.
    """

    escape = CodeSystemConcept(
        {
            "code": "escape",
            "definition": "escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note that this is for when the string itself is escaped.",
            "display": "escape",
        }
    )
    """
    escape

    escape(source, fmt1, fmt2) - change source from one kind of escaping to another (plain, java, xml, json). note that this is for when the string itself is escaped.
    """

    cast = CodeSystemConcept(
        {
            "code": "cast",
            "definition": "cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one and only one target type known.",
            "display": "cast",
        }
    )
    """
    cast

    cast(source, type?) - case source from one type to another. target type can be left as implicit if there is one and only one target type known.
    """

    append = CodeSystemConcept(
        {
            "code": "append",
            "definition": "append(source...) - source is element or string.",
            "display": "append",
        }
    )
    """
    append

    append(source...) - source is element or string.
    """

    translate = CodeSystemConcept(
        {
            "code": "translate",
            "definition": "translate(source, uri_of_map) - use the translate operation.",
            "display": "translate",
        }
    )
    """
    translate

    translate(source, uri_of_map) - use the translate operation.
    """

    reference = CodeSystemConcept(
        {
            "code": "reference",
            "definition": "reference(source : object) - return a string that references the provided tree properly.",
            "display": "reference",
        }
    )
    """
    reference

    reference(source : object) - return a string that references the provided tree properly.
    """

    date_op = CodeSystemConcept(
        {
            "code": "dateOp",
            "definition": "Perform a date operation. *Parameters to be documented*.",
            "display": "dateOp",
        }
    )
    """
    dateOp

    Perform a date operation. *Parameters to be documented*.
    """

    uuid = CodeSystemConcept(
        {
            "code": "uuid",
            "definition": "Generate a random UUID (in lowercase). No Parameters.",
            "display": "uuid",
        }
    )
    """
    uuid

    Generate a random UUID (in lowercase). No Parameters.
    """

    pointer = CodeSystemConcept(
        {
            "code": "pointer",
            "definition": "Return the appropriate string to put in a reference that refers to the resource provided as a parameter.",
            "display": "pointer",
        }
    )
    """
    pointer

    Return the appropriate string to put in a reference that refers to the resource provided as a parameter.
    """

    evaluate = CodeSystemConcept(
        {
            "code": "evaluate",
            "definition": "Execute the supplied FHIRPath expression and use the value returned by that.",
            "display": "evaluate",
        }
    )
    """
    evaluate

    Execute the supplied FHIRPath expression and use the value returned by that.
    """

    cc = CodeSystemConcept(
        {
            "code": "cc",
            "definition": "Create a CodeableConcept. Parameters = (text) or (system. Code[, display]).",
            "display": "cc",
        }
    )
    """
    cc

    Create a CodeableConcept. Parameters = (text) or (system. Code[, display]).
    """

    c = CodeSystemConcept(
        {
            "code": "c",
            "definition": "Create a Coding. Parameters = (system. Code[, display]).",
            "display": "c",
        }
    )
    """
    c

    Create a Coding. Parameters = (system. Code[, display]).
    """

    qty = CodeSystemConcept(
        {
            "code": "qty",
            "definition": "Create a quantity. Parameters = (text) or (value, unit, [system, code]) where text is the natural representation e.g. [comparator]value[space]unit.",
            "display": "qty",
        }
    )
    """
    qty

    Create a quantity. Parameters = (text) or (value, unit, [system, code]) where text is the natural representation e.g. [comparator]value[space]unit.
    """

    id_ = CodeSystemConcept(
        {
            "code": "id",
            "definition": "Create an identifier. Parameters = (system, value[, type]) where type is a code from the identifier type value set.",
            "display": "id",
        }
    )
    """
    id

    Create an identifier. Parameters = (system, value[, type]) where type is a code from the identifier type value set.
    """

    cp = CodeSystemConcept(
        {
            "code": "cp",
            "definition": "Create a contact details. Parameters = (value) or (system, value). If no system is provided, the system should be inferred from the content of the value.",
            "display": "cp",
        }
    )
    """
    cp

    Create a contact details. Parameters = (value) or (system, value). If no system is provided, the system should be inferred from the content of the value.
    """

    class Meta:
        resource = _resource
