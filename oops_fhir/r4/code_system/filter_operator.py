from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["FilterOperator"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class FilterOperator:
    """
    FilterOperator

    The kind of operation to perform as a part of a property based filter.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/filter-operator
    """

    equals_to = CodeSystemConcept(
        {
            "code": "=",
            "definition": "The specified property of the code equals the provided value.",
            "display": "Equals",
        }
    )
    """
    Equals

    The specified property of the code equals the provided value.
    """

    is_a = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "The definition of is-a is that all the properties of the value are true for the specified property of the code, which means that a code has an is-a relationship with itself. To exclude the root code, use descendent-of",
                }
            ],
            "code": "is-a",
            "definition": "Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value, including the provided concept itself (include descendant codes and self).",
            "display": "Is A (by subsumption)",
        }
    )
    """
    Is A (by subsumption)

    Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value, including the provided concept itself (include descendant codes and self).
    """

    descendent_of = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": 'The definition of is-a is that all the properties of the value are true for the specified property of the code. \n\nSpelling note: "descendant" is a more correct spelling, but the spelling "descendent" is maintained in the code for backwards compatibility reasons',
                }
            ],
            "code": "descendent-of",
            "definition": "Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value, excluding the provided concept itself i.e. include descendant codes only).",
            "display": "Descendent Of (by subsumption)",
        }
    )
    """
    Descendent Of (by subsumption)

    Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value, excluding the provided concept itself i.e. include descendant codes only).
    """

    is_not_a = CodeSystemConcept(
        {
            "code": "is-not-a",
            "definition": "The specified property of the code does not have an is-a relationship with the provided value.",
            "display": "Not (Is A) (by subsumption)",
        }
    )
    """
    Not (Is A) (by subsumption)

    The specified property of the code does not have an is-a relationship with the provided value.
    """

    regex = CodeSystemConcept(
        {
            "code": "regex",
            "definition": "The specified property of the code  matches the regex specified in the provided value.",
            "display": "Regular Expression",
        }
    )
    """
    Regular Expression

    The specified property of the code  matches the regex specified in the provided value.
    """

    in_ = CodeSystemConcept(
        {
            "code": "in",
            "definition": "The specified property of the code is in the set of codes or concepts specified in the provided value (comma separated list).",
            "display": "In Set",
        }
    )
    """
    In Set

    The specified property of the code is in the set of codes or concepts specified in the provided value (comma separated list).
    """

    not_in = CodeSystemConcept(
        {
            "code": "not-in",
            "definition": "The specified property of the code is not in the set of codes or concepts specified in the provided value (comma separated list).",
            "display": "Not in Set",
        }
    )
    """
    Not in Set

    The specified property of the code is not in the set of codes or concepts specified in the provided value (comma separated list).
    """

    generalizes = CodeSystemConcept(
        {
            "extension": [
                {
                    "url": "http://hl7.org/fhir/StructureDefinition/codesystem-concept-comments",
                    "valueString": "The definition of is-a is that all the properties of the value are true for the specified property of the code, which means that a code has an is-a relationship with itself. To exclude the root code, add it explicitly to as an exclude",
                }
            ],
            "code": "generalizes",
            "definition": "Includes all concept ids that have a transitive is-a relationship from the concept Id provided as the value, including the provided concept itself (i.e. include ancestor codes and self).",
            "display": "Generalizes (by Subsumption)",
        }
    )
    """
    Generalizes (by Subsumption)

    Includes all concept ids that have a transitive is-a relationship from the concept Id provided as the value, including the provided concept itself (i.e. include ancestor codes and self).
    """

    exists = CodeSystemConcept(
        {
            "code": "exists",
            "definition": "The specified property of the code has at least one value (if the specified value is true; if the specified value is false, then matches when the specified property of the code has no values).",
            "display": "Exists",
        }
    )
    """
    Exists

    The specified property of the code has at least one value (if the specified value is true; if the specified value is false, then matches when the specified property of the code has no values).
    """

    class Meta:
        resource = _resource
