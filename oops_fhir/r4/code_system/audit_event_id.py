from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["AuditEventID"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class AuditEventID:
    """
    Audit Event ID

    Event Types for Audit Events - defined by DICOM with some FHIR specific
additions.

    Status: active - Version: 4.0.1

    Copyright These codes are excerpted from Digital Imaging and Communications in Medicine (DICOM) Standard, Part 16: Content Mapping Resource, Copyright © 2011 by the National Electrical Manufacturers Association.

    http://terminology.hl7.org/CodeSystem/audit-event-type
    """

    rest = CodeSystemConcept(
        {
            "code": "rest",
            "definition": "Audit Event: Execution of a RESTful operation as defined by FHIR.",
            "display": "RESTful Operation",
        }
    )
    """
    RESTful Operation

    Audit Event: Execution of a RESTful operation as defined by FHIR.
    """

    class Meta:
        resource = _resource
