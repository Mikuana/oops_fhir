from pathlib import Path

from fhir.resources.codesystem import CodeSystem

from oops_fhir.utils import CodeSystemConcept


__all__ = ["DICOMAuditMessageRecordLifecycleEvents"]

_resource = CodeSystem.parse_file(Path(__file__).with_suffix(".json"))


class DICOMAuditMessageRecordLifecycleEvents:
    """
    None

    Attached is vocabulary for the record lifecycle events, as per DICOM
Audit Message,

    Status: active - Version: 20100826

    Copyright These codes are excerpted from Digital Imaging and Communications in Medicine (DICOM) Standard, Part 16: Content Mapping Resource, Copyright © 2011 by the National Electrical Manufacturers Association.

    http://terminology.hl7.org/CodeSystem/dicom-audit-lifecycle
    """

    one = CodeSystemConcept({"code": "1", "display": "Origination / Creation"})
    """
    Origination / Creation

    
    """

    two = CodeSystemConcept({"code": "2", "display": "Import / Copy"})
    """
    Import / Copy

    
    """

    three = CodeSystemConcept({"code": "3", "display": "Amendment"})
    """
    Amendment

    
    """

    four = CodeSystemConcept({"code": "4", "display": "Verification"})
    """
    Verification

    
    """

    five = CodeSystemConcept({"code": "5", "display": "Translation"})
    """
    Translation

    
    """

    six = CodeSystemConcept({"code": "6", "display": "Access / Use"})
    """
    Access / Use

    
    """

    seven = CodeSystemConcept({"code": "7", "display": "De-identification"})
    """
    De-identification

    
    """

    eight = CodeSystemConcept(
        {"code": "8", "display": "Aggregation / summarization / derivation"}
    )
    """
    Aggregation / summarization / derivation

    
    """

    nine = CodeSystemConcept({"code": "9", "display": "Report"})
    """
    Report

    
    """

    one0 = CodeSystemConcept({"code": "10", "display": "Export"})
    """
    Export

    
    """

    one1 = CodeSystemConcept({"code": "11", "display": "Disclosure"})
    """
    Disclosure

    
    """

    one2 = CodeSystemConcept({"code": "12", "display": "Receipt of disclosure"})
    """
    Receipt of disclosure

    
    """

    one3 = CodeSystemConcept({"code": "13", "display": "Archiving"})
    """
    Archiving

    
    """

    one4 = CodeSystemConcept({"code": "14", "display": "Logical deletion"})
    """
    Logical deletion

    
    """

    one5 = CodeSystemConcept(
        {"code": "15", "display": "Permanent erasure / Physical destruction"}
    )
    """
    Permanent erasure / Physical destruction

    
    """

    class Meta:
        resource = _resource
