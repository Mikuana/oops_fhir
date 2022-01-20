from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3styleType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3styleType:
    """
    v3 Code System styleType

     <ns1:p>The style code is used within the CDA/SPL narrative block to
give the instance author some control over various aspects of
style</ns1:p>

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-styleType
    """

    underscore_font_style = CodeSystemConcept(
        {
            "code": "_FontStyle",
            "concept": [
                {
                    "code": "bold",
                    "definition": "Render with a bold font",
                    "display": "Bold Font",
                },
                {
                    "code": "emphasis",
                    "definition": "Render with with some type of emphasis",
                    "display": "Emphasised Font",
                },
                {
                    "code": "italics",
                    "definition": "Render italicized",
                    "display": "Italics Font",
                },
                {
                    "code": "underline",
                    "definition": "Render with an underline font",
                    "display": "Underline Font",
                },
            ],
            "definition": "Defines font rendering characteristics",
            "display": "Font Style",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Font Style

    Defines font rendering characteristics
    """

    underscore_list_style = CodeSystemConcept(
        {
            "code": "_ListStyle",
            "concept": [
                {
                    "code": "_OrderedListStyle",
                    "concept": [
                        {
                            "code": "Arabic",
                            "definition": "List is ordered using Arabic numerals: 1, 2, 3",
                            "display": "Arabic",
                        },
                        {
                            "code": "BigAlpha",
                            "definition": "List is ordered using big alpha characters: A, B, C",
                            "display": "Big Alpha",
                        },
                        {
                            "code": "BigRoman",
                            "definition": "List is ordered using big Roman numerals: I, II, III",
                            "display": "Big Roman",
                        },
                        {
                            "code": "LittleAlpha",
                            "definition": "List is order using little alpha characters: a, b, c",
                            "display": "Little Alpha",
                        },
                        {
                            "code": "LittleRoman",
                            "definition": "List is ordered using little Roman numerals: i, ii, iii",
                            "display": "Little Roman",
                        },
                    ],
                    "definition": "Defines rendering characteristics for ordered lists",
                    "display": "Ordered List Style",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
                {
                    "code": "_UnorderedListStyle",
                    "concept": [
                        {
                            "code": "Circle",
                            "definition": "List bullets are hollow discs",
                            "display": "Circle",
                        },
                        {
                            "code": "Disc",
                            "definition": "List bullets are simple solid discs",
                            "display": "Disc",
                        },
                        {
                            "code": "Square",
                            "definition": "List bullets are solid squares",
                            "display": "Square",
                        },
                    ],
                    "definition": "Defines rendering characteristics for unordered lists",
                    "display": "Unordered List Style",
                    "property": [{"code": "notSelectable", "valueBoolean": True}],
                },
            ],
            "definition": "Defines list rendering characteristics",
            "display": "List Style",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    List Style

    Defines list rendering characteristics
    """

    underscore_table_rule_style = CodeSystemConcept(
        {
            "code": "_TableRuleStyle",
            "concept": [
                {
                    "code": "Botrule",
                    "definition": "Render cell with rule on bottom",
                    "display": "Bottom Rule",
                },
                {
                    "code": "Lrule",
                    "definition": "Render cell with left-sided rule",
                    "display": "Left-sided rule",
                },
                {
                    "code": "Rrule",
                    "definition": "Render cell with right-sided rule",
                    "display": "Right-sided rule",
                },
                {
                    "code": "Toprule",
                    "definition": "Render cell with rule on top",
                    "display": "Top Rule",
                },
            ],
            "definition": "Defines table cell rendering characteristics",
            "display": "Table Rule Style",
            "property": [{"code": "notSelectable", "valueBoolean": True}],
        }
    )
    """
    Table Rule Style

    Defines table cell rendering characteristics
    """

    class Meta:
        resource = _resource
