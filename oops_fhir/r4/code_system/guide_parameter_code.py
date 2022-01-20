from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GuideParameterCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GuideParameterCode:
    """
    GuideParameterCode

    Code of parameter that is input to the guide.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/guide-parameter-code
    """

    apply = CodeSystemConcept(
        {
            "code": "apply",
            "definition": "If the value of this string 0..* parameter is one of the metadata fields then all conformance resources will have any specified [Resource].[field] overwritten with the ImplementationGuide.[field], where field is one of: version, date, status, publisher, contact, copyright, experimental, jurisdiction, useContext.",
            "display": "Apply Metadata Value",
        }
    )
    """
    Apply Metadata Value

    If the value of this string 0..* parameter is one of the metadata fields then all conformance resources will have any specified [Resource].[field] overwritten with the ImplementationGuide.[field], where field is one of: version, date, status, publisher, contact, copyright, experimental, jurisdiction, useContext.
    """

    path_resource = CodeSystemConcept(
        {
            "code": "path-resource",
            "definition": "The value of this string 0..* parameter is a subfolder of the build context's location that is to be scanned to load resources. Scope is (if present) a particular resource type.",
            "display": "Resource Path",
        }
    )
    """
    Resource Path

    The value of this string 0..* parameter is a subfolder of the build context's location that is to be scanned to load resources. Scope is (if present) a particular resource type.
    """

    path_pages = CodeSystemConcept(
        {
            "code": "path-pages",
            "definition": "The value of this string 0..1 parameter is a subfolder of the build context's location that contains files that are part of the html content processed by the builder.",
            "display": "Pages Path",
        }
    )
    """
    Pages Path

    The value of this string 0..1 parameter is a subfolder of the build context's location that contains files that are part of the html content processed by the builder.
    """

    path_tx_cache = CodeSystemConcept(
        {
            "code": "path-tx-cache",
            "definition": "The value of this string 0..1 parameter is a subfolder of the build context's location that is used as the terminology cache. If this is not present, the terminology cache is on the local system, not under version control.",
            "display": "Terminology Cache Path",
        }
    )
    """
    Terminology Cache Path

    The value of this string 0..1 parameter is a subfolder of the build context's location that is used as the terminology cache. If this is not present, the terminology cache is on the local system, not under version control.
    """

    expansion_parameter = CodeSystemConcept(
        {
            "code": "expansion-parameter",
            "definition": "The value of this string 0..* parameter is a parameter (name=value) when expanding value sets for this implementation guide. This is particularly used to specify the versions of published terminologies such as SNOMED CT.",
            "display": "Expansion Profile",
        }
    )
    """
    Expansion Profile

    The value of this string 0..* parameter is a parameter (name=value) when expanding value sets for this implementation guide. This is particularly used to specify the versions of published terminologies such as SNOMED CT.
    """

    rule_broken_links = CodeSystemConcept(
        {
            "code": "rule-broken-links",
            "definition": 'The value of this string 0..1 parameter is either "warning" or "error" (default = "error"). If the value is "warning" then IG build tools allow the IG to be considered successfully build even when there is no internal broken links.',
            "display": "Broken Links Rule",
        }
    )
    """
    Broken Links Rule

    The value of this string 0..1 parameter is either "warning" or "error" (default = "error"). If the value is "warning" then IG build tools allow the IG to be considered successfully build even when there is no internal broken links.
    """

    generate_xml = CodeSystemConcept(
        {
            "code": "generate-xml",
            "definition": "The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in XML format. If not present, the Publication Tool decides whether to generate XML.",
            "display": "Generate XML",
        }
    )
    """
    Generate XML

    The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in XML format. If not present, the Publication Tool decides whether to generate XML.
    """

    generate_json = CodeSystemConcept(
        {
            "code": "generate-json",
            "definition": "The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in JSON format. If not present, the Publication Tool decides whether to generate JSON.",
            "display": "Generate JSON",
        }
    )
    """
    Generate JSON

    The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in JSON format. If not present, the Publication Tool decides whether to generate JSON.
    """

    generate_turtle = CodeSystemConcept(
        {
            "code": "generate-turtle",
            "definition": "The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in Turtle format. If not present, the Publication Tool decides whether to generate Turtle.",
            "display": "Generate Turtle",
        }
    )
    """
    Generate Turtle

    The value of this boolean 0..1 parameter specifies whether the IG publisher creates examples in Turtle format. If not present, the Publication Tool decides whether to generate Turtle.
    """

    html_template = CodeSystemConcept(
        {
            "code": "html-template",
            "definition": "The value of this string singleton parameter is the name of the file to use as the builder template for each generated page (see templating).",
            "display": "HTML Template",
        }
    )
    """
    HTML Template

    The value of this string singleton parameter is the name of the file to use as the builder template for each generated page (see templating).
    """

    class Meta:
        resource = _resource
