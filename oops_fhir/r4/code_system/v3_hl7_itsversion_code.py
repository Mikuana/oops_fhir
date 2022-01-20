from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3hl7ITSVersionCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3hl7ITSVersionCode:
    """
    v3 Code System hl7ITSVersionCode

     HL7 implementation technology specification versions. These codes will
document the ITS type and version for message encoding. The code will
appear in the instances based upon rules expressed in the ITS, and do
not appear in the abstract message, either as it is presented to
received from the ITS.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-hl7ITSVersionCode
    """

    xmlv1_pr1 = CodeSystemConcept(
        {
            "code": "XMLV1PR1",
            "definition": "XML ITS version 1 pre-release 1.",
            "display": "XMLV1PR1",
        }
    )
    """
    XMLV1PR1

    XML ITS version 1 pre-release 1.
    """

    class Meta:
        resource = _resource
