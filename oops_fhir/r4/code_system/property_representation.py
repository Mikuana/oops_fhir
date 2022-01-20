from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["PropertyRepresentation"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class PropertyRepresentation:
    """
    PropertyRepresentation

    How a property is represented when serialized.

    Status: active - Version: 4.0.1

    Copyright None

    http://hl7.org/fhir/property-representation
    """

    xml_attr = CodeSystemConcept(
        {
            "code": "xmlAttr",
            "definition": "In XML, this property is represented as an attribute not an element.",
            "display": "XML Attribute",
        }
    )
    """
    XML Attribute

    In XML, this property is represented as an attribute not an element.
    """

    xml_text = CodeSystemConcept(
        {
            "code": "xmlText",
            "definition": "This element is represented using the XML text attribute (primitives only).",
            "display": "XML Text",
        }
    )
    """
    XML Text

    This element is represented using the XML text attribute (primitives only).
    """

    type_attr = CodeSystemConcept(
        {
            "code": "typeAttr",
            "definition": "The type of this element is indicated using xsi:type.",
            "display": "Type Attribute",
        }
    )
    """
    Type Attribute

    The type of this element is indicated using xsi:type.
    """

    cda_text = CodeSystemConcept(
        {
            "code": "cdaText",
            "definition": "Use CDA narrative instead of XHTML.",
            "display": "CDA Text Format",
        }
    )
    """
    CDA Text Format

    Use CDA narrative instead of XHTML.
    """

    xhtml = CodeSystemConcept(
        {
            "code": "xhtml",
            "definition": "The property is represented using XHTML.",
            "display": "XHTML",
        }
    )
    """
    XHTML

    The property is represented using XHTML.
    """

    class Meta:
        resource = _resource
