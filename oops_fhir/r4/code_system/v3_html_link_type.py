from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3HtmlLinkType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3HtmlLinkType:
    """
    v3 Code System HtmlLinkType

     HtmlLinkType values are drawn from HTML 4.0 and describe the
relationship between the current document and the anchor that is the
target of the link

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-HtmlLinkType
    """

    alternate = CodeSystemConcept(
        {
            "code": "alternate",
            "definition": "Designates substitute versions for the document in which the link occurs. When used together with the lang attribute, it implies a translated version of the document. When used together with the media attribute, it implies a version designed for a different medium (or media).",
            "display": "alternate",
        }
    )
    """
    alternate

    Designates substitute versions for the document in which the link occurs. When used together with the lang attribute, it implies a translated version of the document. When used together with the media attribute, it implies a version designed for a different medium (or media).
    """

    appendix = CodeSystemConcept(
        {
            "code": "appendix",
            "definition": "Refers to a document serving as an appendix in a collection of documents.",
            "display": "appendix",
        }
    )
    """
    appendix

    Refers to a document serving as an appendix in a collection of documents.
    """

    bookmark = CodeSystemConcept(
        {
            "code": "bookmark",
            "definition": "Refers to a bookmark. A bookmark is a link to a key entry point within an extended document. The title attribute may be used, for example, to label the bookmark. Note that several bookmarks may be defined in each document.",
            "display": "bookmark",
        }
    )
    """
    bookmark

    Refers to a bookmark. A bookmark is a link to a key entry point within an extended document. The title attribute may be used, for example, to label the bookmark. Note that several bookmarks may be defined in each document.
    """

    chapter = CodeSystemConcept(
        {
            "code": "chapter",
            "definition": "Refers to a document serving as a chapter in a collection of documents.",
            "display": "chapter",
        }
    )
    """
    chapter

    Refers to a document serving as a chapter in a collection of documents.
    """

    contents = CodeSystemConcept(
        {
            "code": "contents",
            "definition": 'Refers to a document serving as a table of contents. Some user agents also support the synonym ToC (from "Table of Contents").',
            "display": "contents",
        }
    )
    """
    contents

    Refers to a document serving as a table of contents. Some user agents also support the synonym ToC (from "Table of Contents").
    """

    copyright_ = CodeSystemConcept(
        {
            "code": "copyright",
            "definition": "Refers to a copyright statement for the current document.",
            "display": "copyright",
        }
    )
    """
    copyright

    Refers to a copyright statement for the current document.
    """

    glossary = CodeSystemConcept(
        {
            "code": "glossary",
            "definition": "Refers to a document providing a glossary of terms that pertain to the current document.",
            "display": "glossary",
        }
    )
    """
    glossary

    Refers to a document providing a glossary of terms that pertain to the current document.
    """

    help_ = CodeSystemConcept(
        {
            "code": "help",
            "definition": "Refers to a document offering help (more information, links to other sources of information, etc.).",
            "display": "help",
        }
    )
    """
    help

    Refers to a document offering help (more information, links to other sources of information, etc.).
    """

    index = CodeSystemConcept(
        {
            "code": "index",
            "definition": "Refers to a document providing an index for the current document.",
            "display": "index",
        }
    )
    """
    index

    Refers to a document providing an index for the current document.
    """

    next_ = CodeSystemConcept(
        {
            "code": "next",
            "definition": 'Refers to the next document in a linear sequence of documents. User agents may choose to preload the "next" document, to reduce the perceived load time.',
            "display": "next",
        }
    )
    """
    next

    Refers to the next document in a linear sequence of documents. User agents may choose to preload the "next" document, to reduce the perceived load time.
    """

    prev = CodeSystemConcept(
        {
            "code": "prev",
            "definition": 'Refers to the previous document in an ordered series of documents. Some user agents also support the synonym "Previous".',
            "display": "prev",
        }
    )
    """
    prev

    Refers to the previous document in an ordered series of documents. Some user agents also support the synonym "Previous".
    """

    section = CodeSystemConcept(
        {
            "code": "section",
            "definition": "Refers to a document serving as a section in a collection of documents.",
            "display": "section",
        }
    )
    """
    section

    Refers to a document serving as a section in a collection of documents.
    """

    start = CodeSystemConcept(
        {
            "code": "start",
            "definition": "Refers to the first document in a collection of documents. This link type tells search engines which document is considered by the author to be the starting point of the collection.",
            "display": "start",
        }
    )
    """
    start

    Refers to the first document in a collection of documents. This link type tells search engines which document is considered by the author to be the starting point of the collection.
    """

    stylesheet = CodeSystemConcept(
        {
            "code": "stylesheet",
            "definition": 'Refers to an external style sheet. See the section on external style sheets for details. This is used together with the link type "Alternate" for user-selectable alternate style sheets.',
            "display": "stylesheet",
        }
    )
    """
    stylesheet

    Refers to an external style sheet. See the section on external style sheets for details. This is used together with the link type "Alternate" for user-selectable alternate style sheets.
    """

    subsection = CodeSystemConcept(
        {
            "code": "subsection",
            "definition": "Refers to a document serving as a subsection in a collection of documents.",
            "display": "subsection",
        }
    )
    """
    subsection

    Refers to a document serving as a subsection in a collection of documents.
    """

    class Meta:
        resource = _resource
