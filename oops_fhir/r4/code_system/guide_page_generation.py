from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["GuidePageGeneration"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class GuidePageGeneration:
    """
    GuidePageGeneration

    A code that indicates how the page is generated.

    Status: draft - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/guide-page-generation
    """

    html = CodeSystemConcept(
        {
            "code": "html",
            "definition": "Page is proper xhtml with no templating.  Will be brought across unchanged for standard post-processing.",
            "display": "HTML",
        }
    )
    """
    HTML

    Page is proper xhtml with no templating.  Will be brought across unchanged for standard post-processing.
    """

    markdown = CodeSystemConcept(
        {
            "code": "markdown",
            "definition": "Page is markdown with templating.  Will use the template to create a file that imports the markdown file prior to post-processing.",
            "display": "Markdown",
        }
    )
    """
    Markdown

    Page is markdown with templating.  Will use the template to create a file that imports the markdown file prior to post-processing.
    """

    xml = CodeSystemConcept(
        {
            "code": "xml",
            "definition": "Page is xml with templating.  Will use the template to create a file that imports the source file and run the nominated XSLT transform (see parameters) if present prior to post-processing.",
            "display": "XML",
        }
    )
    """
    XML

    Page is xml with templating.  Will use the template to create a file that imports the source file and run the nominated XSLT transform (see parameters) if present prior to post-processing.
    """

    generated = CodeSystemConcept(
        {
            "code": "generated",
            "definition": "Page will be generated by the publication process - no source to bring across.",
            "display": "Generated",
        }
    )
    """
    Generated

    Page will be generated by the publication process - no source to bring across.
    """

    class Meta:
        resource = _resource