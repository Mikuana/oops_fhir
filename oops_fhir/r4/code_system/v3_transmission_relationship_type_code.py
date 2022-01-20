from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["v3TransmissionRelationshipTypeCode"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class v3TransmissionRelationshipTypeCode:
    """
    v3 Code System TransmissionRelationshipTypeCode

      Description:  A code specifying the meaning and purpose of every
TransmissionRelationship instance. Each of its values implies specific
constraints to what kinds of Transmission objects can be related and in
which way.

    Status: active - Version: 2018-08-12

    Copyright None

    http://terminology.hl7.org/CodeSystem/v3-TransmissionRelationshipTypeCode
    """

    seql = CodeSystemConcept(
        {
            "code": "SEQL",
            "definition": "Description:A transmission relationship indicating that the source transmission follows the target transmission.",
            "display": "sequence",
        }
    )
    """
    sequence

    Description:A transmission relationship indicating that the source transmission follows the target transmission.
    """

    class Meta:
        resource = _resource
