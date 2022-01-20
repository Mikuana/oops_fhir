from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7ITSType"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7ITSType:
    """
    v3 Code System hl7ITSType

      Description:  Codes identifying types of HL7 Implementation Technology
Specifications

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7ITSType
    """

    uml = CodeSystemConcept(
        {
            "code": "UML",
            "definition": "Description: ITS based on the Universal Modeling Language.",
            "display": "universal modeling language",
        }
    )
    """
    universal modeling language

    Description: ITS based on the Universal Modeling Language.
    """

    xml = CodeSystemConcept(
        {
            "code": "XML",
            "definition": "Description: ITS based on the Extensible Markup Language.",
            "display": "extensible markup language",
        }
    )
    """
    extensible markup language

    Description: ITS based on the Extensible Markup Language.
    """

    class Meta:
        resource = _resource
